import csv
from blackjack import *
from inventory import *
from newgame import *
from accounts import *

print("\n----------------------------------------------------------------")
print("                ♠♣♥♦ WELCOME TO BLACKJACK! ♠♣♥♦")
print("                          MAIN MENU")
print("----------------------------------------------------------------")

#updates balance into database
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

def main_menu(player, balance):
    print(
        "(1) Start new game\n(2) Check balance\n(3) Add balance\n(4) Exit game"
        )
    menu_input = input("What would you like to do? ")
    while menu_input not in ['1', '2', '3', '4']: #ask for new input if not valid
        menu_input = input("Invalid input, please choose a valid option: ")
    if menu_input == '1':
        newgame(player, balance)
    elif menu_input == '2':
        print("Your balance is: " + str(balance.check_value()))
        main_menu(player, balance)
    elif menu_input == '3':
        print("How much do you want to add? ")
        while True:
            try: #returns exception if input is not a number
                added_balance = float(input())
                balance.add_value(added_balance)
                print(f"You have added {added_balance} to your balance!")
                break
            except:
                print("Invalid input, please enter a number: ")
        write_newbalance(player, balance.check_value())
        main_menu(player, balance)
    elif menu_input == '4':
        quit()
