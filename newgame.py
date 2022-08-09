from blackjack import *
from inventory import *

# FUNCTION DEFINITIONS:

def newgame(player_chips):
    def hit(deck, hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()


    def hit_or_stand(deck, hand):
        global playing

        while True:
            x = input("\nWould you like to Hit or Stand? Enter [h/s] ")
            

            if x[0].lower() == "h":
                hit(deck, hand)  # hit() function defined above

            elif x[0].lower() == "s":
                print("Player stands. Dealer is playing.")
                playing = False

            else:
                print("Sorry, Invalid Input. Please enter [h/s].")
                continue
            break

    def gamble():
        valid_bet = False
        while valid_bet == False:
            bet = int(input("Place a bet: "))
            player_balance = player_chips.check_value()
            if player_balance < bet:
                print("Player doesn't have enough chips!")
            else:
                player_chips.place_bet(bet)
                break
        return bet
        
    def show_some(player, dealer):
        print("\nPlayer's Hand:", *player.cards, sep="\n ")
        print("Player's Hand =", player.value)
        print("\nDealer's Hand:")
        print(" <card hidden>")
        print("", dealer.cards[1])


    def show_all(player, dealer):
        print("\nPlayer's Hand:", *player.cards, sep="\n ")
        print("Player's Hand =", player.value)
        print("\nDealer's Hand:", *dealer.cards, sep="\n ")
        print("Dealer's Hand =", dealer.value)


    def player_busts(player, dealer):
        print("\n--- Player busts! ---")
        print(f"Player lost {bet}!")


    def player_wins(player, dealer):
        print("\n--- Player has blackjack! You win! ---")
        print(f"Player wins {bet}!")
        player_chips.add_value(bet)


    def dealer_busts(player, dealer):
        print("\n--- Dealer busts! You win! ---")
        print(f"Player wins {bet}!")
        player_chips.add_value(bet)

    def dealer_wins(player, dealer):
        print("\n--- Dealer wins! ---")
        print(f"Player lost {bet}!")

    def push(player, dealer):
        print("\nIts a tie!")
        print(f"Player keeps {bet}.")
        player_chips.add_value(bet)


    # GAMEPLAY!

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
        
        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Show the cards:
        show_some(player_hand, dealer_hand)

        global playing
        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)
            
            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand)
                break

        # If Player hasn't busted, play Dealer's hand
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all cards
            time.sleep(1)
            print("\n----------------------------------------------------------------")
            print("                     ★ Final Results ★")
            print("----------------------------------------------------------------")

            show_all(player_hand, dealer_hand)

            # Test different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand)

            else:
                push(player_hand, dealer_hand)

        # Ask to play again
        new_game = input("\nPlay another hand? [Y/N] ")
        while new_game.lower() not in ["y", "n"]:
            new_game = input("Invalid Input. Please enter 'y' or 'n' ")
        if new_game[0].lower() == "y":
            playing = True
            continue
        else:
            break
