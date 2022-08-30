from blackjack import *
from inventory import *
from newgame import *

print("\n----------------------------------------------------------------")
print("                ♠♣♥♦ WELCOME TO BLACKJACK! ♠♣♥♦")
print("                          MAIN MENU")
print("----------------------------------------------------------------")

    
def main_menu(player):
    print(
        "(1) Start new game\n(2) Check balance\n(3) Add balance"
        )
    menu_input = input("What would you like to do? ")
    while menu_input not in ['1', '2', '3']:
        menu_input = input("Invalid input, please choose a valid option: ")
    if menu_input == '1':
        newgame(player)
    elif menu_input == '2':
        print("Your balance is: " + str(player.check_value()))
        main_menu()
    elif menu_input == '3':
        print("How much do you want to add? ")
        while True:
            try:
                added_balance = float(input())
                player.add_value(added_balance)
                print(f"You have added {added_balance} to your balance!")
                break
            except:
                print("Invalid input, please enter a number: ")
        main_menu()
