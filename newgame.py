import csv
from blackjack import *
from inventory import *

#updates new balance into database
def write_newbalance(player, new_balance):
    with open("database.txt", mode='r') as database:
        database1_csv = csv.reader(database, delimiter=',')
        data = []
        for line in database1_csv: #iterates through database for right account
            if player.lower() == line[0].lower(): 
                data.append(f"{line[0]},{line[1]},{new_balance}\n")
            else:
                data.append(line)
                    
    with open("database.txt", mode='w') as database: #updates database
        database.writelines(data)

#starts a new blackjack game
def newgame(username, balance):
    #draw card from deck
    def hit(deck, hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()

    #gives the choice of hitting or standing
    def hit_or_stand(deck, hand):
        global playing

        while True:
            x = input("\nWould you like to Hit or Stand? Enter [h/s] ")
            
            if x[0].lower() == "h":
                hit(deck, hand)  #hit() function defined above

            elif x[0].lower() == "s":
                print("Player stands. Dealer is playing.")
                playing = False

            else:
                print("Sorry, Invalid Input. Please enter [h/s].")
                continue
            break

    #function to place a bet
    def gamble():
        while True:
            print("Place a bet: ")
            try: #returns exception if input is not a number
                bet = int(input())
                break
            except:
                print("Invalid input, please enter a number: ")
        player_balance = balance.check_value()
        while player_balance < bet: #check if player can afford his bet
            while True:
                print(f"You only have a balance of {player_balance}, please enter an amount of chips you have:")
                try:
                    bet = int(input())
                    break
                except: #returns exception if input is not a number
                    print("Invalid input, please enter a number: ")
        balance.place_bet(bet)
        write_newbalance(username, balance.check_value())
        return bet
        
    def show_some(player, dealer): #showing player's hand and dealer's hand during game
        print("\nPlayer's Hand:", *player.cards, sep="\n ")
        print("Player's Hand =", player.value)
        print("\nDealer's Hand:")
        print(" <card hidden>")
        print("", dealer.cards[1])
        

    def show_all(player, dealer): #showing player's hand and dealer's hand after game
        print("\nPlayer's Hand:", *player.cards, sep="\n ")
        print("Player's Hand =", player.value)
        print("\nDealer's Hand:", *dealer.cards, sep="\n ")
        print("Dealer's Hand =", dealer.value)


    def player_busts(player, dealer): #when player's value > 21
        print("\n--- Player busts! ---")
        print(f"{username} lost {bet}!")
        print(f"Your balance is {balance.check_value()}")

    def player_wins(player, dealer): #when player's value > dealer's value
        print("\n--- Player has blackjack! You win! ---")
        print(f"{username} wins {bet}!")
        balance.add_value(2*bet)
        print(f"Your balance is {balance.check_value()}")

    def dealer_busts(player, dealer): #when dealer's value > 21
        print("\n--- Dealer busts! You win! ---")
        print(f"{username} wins {bet}!")
        balance.add_value(2*bet)
        print(f"Your balance is {balance.check_value()}")

    def dealer_wins(player, dealer): #when player's value < dealer's value
        print("\n--- Dealer wins! ---")
        print(f"{username} lost {bet}!")
        print(f"Your balance is {balance.check_value()}")

    def push(player, dealer): #when player's and dealer's values are the same
        print("\nIts a tie!")
        print(f"{username} keeps {bet}.")
        balance.add_value(bet)
        print(f"Your balance is {balance.check_value()}")


    #GAMEPLAY!

    while True:
        print("\n----------------------------------------------------------------")
        print("                ♠♣♥♦ WELCOME TO BLACKJACK! ♠♣♥♦")
        print("                          Lets Play!")
        print("----------------------------------------------------------------")
        print(
            "Game Rules:  Get as close to 21 as you can without going over!\n\
            Dealer hits until he/she reaches 17.\n\
            Aces count as 1 or 11."
        )
        bet = gamble()
        
        #Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand() #creates player's hand and deals 2 cards
        player_hand.add_card(deck.deal()) 
        player_hand.add_card(deck.deal())

        dealer_hand = Hand() #creates dealer's hand and deals 2 cards
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        #Show the cards:
        show_some(player_hand, dealer_hand)

        global playing
        while playing:  #recall this variable from our hit_or_stand function

            #Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)

            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand)
                break

        #If Player hasn't busted, play Dealer's hand
        if player_hand.value <= 21:

            #determines whether dealer hits or stands
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            #Show all cards
            time.sleep(1)
            print("\n----------------------------------------------------------------")
            print("                     ★ Final Results ★")
            print("----------------------------------------------------------------")

            show_all(player_hand, dealer_hand)

            #Test different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand)

            else:
                push(player_hand, dealer_hand)

        #updates balance after game
        write_newbalance(username, balance.check_value())
        
        #Ask to play again
        new_game = input("\nPlay another hand? [Y/N] ")
        while new_game.lower() not in ["y", "n"]:
            new_game = input("Invalid Input. Please enter 'y' or 'n' ")
        if new_game[0].lower() == "y":
            playing = True
            continue
        else:
            break
