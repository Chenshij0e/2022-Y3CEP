from blackjack import *
from inventory import *
from newgame import *

player = Inventory(500)

print("\n----------------------------------------------------------------")
print("                ♠♣♥♦ WELCOME TO BLACKJACK! ♠♣♥♦")
print("                          MAIN MENU")
print("----------------------------------------------------------------")
print(
        "(1) Start new game\n(2) Check balance\n(3) Add balance"
        )
    
def main_menu():
    menu_input = input("What would you like to do? ")
    while menu_input not in ['1', '2', '3']:
        menu_input = input("Invalid input, please choose a valid option. ")
    if menu_input == '1':
        newgame(player)
    elif menu_input == '2':
        print("Your balance is: " + str(player.check_value()))
        main_menu()
    elif menu_input == '3':
        added_balance = float(input("How much do you want to add? "))
        player.add_value(added_balance)
        print(f"You have added {added_balance} to your balance!")
        main_menu()


loop = 1     

while loop == 1:
    main_menu()
