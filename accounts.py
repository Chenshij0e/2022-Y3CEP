from inventory import *
import csv
from mainmenu import *

class Account:

    def __init__(self, user, password):
        self.username = user
        self.password = password
        self.balance = Inventory(500)

    def add_username(self, user):
        self.username = user

    def add_password(self, password):
        self.password = password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_balance(self):
        return self.balance.check_value()

    def get_balanceobj(self):
        return self.balance

    def __str__(self):
        return self.username

def signup():
    user = input("Username: ")
    while len(user) < 3 or len(user) > 20 or user.replace('_', '').isalnum() == False:
        user = input("Please choose a username that is 3 to 20 characters long,\nwith alphanumeric characters and underscores only:\n")
    with open("database.txt") as database:
        database_csv = csv.reader(database, delimiter=',')
        for line in database_csv:
            while user.lower() == line[0].lower():
                user = input("That username is already taken! Please try again:\n")
    password = input("Password: ")
    while len(password) < 6:
        password = input("Please choose a password that is at least 6 characters long:\n")
    global acc
    acc = Account(user, password)
    with open("database.txt", mode='a') as database:
        database.write(f"{acc.get_username()},{acc.get_password()},{acc.get_balance()}\n")


def login():
    user_input = input("Username: ")
    password_input = input("Password: ")
    with open("database.txt") as database:
        database_csv = csv.reader(database, delimiter=',')
        for line in database_csv:
            if user_input.lower() == line[0].lower():
                if password_input == line[1]:
                    global acc
                    acc = Account(user_input, password_input)
                    return True
        print("Username or password is incorrect.")
        return False

def signup_or_login():
    
    print("(a) Sign up")
    print("(b) Login")
    choice = input("What would you like to do?\n")
    while choice not in ['a', 'b']:
        choice = input("Invalid option, please try again: ")
    if choice == 'a':
        signup()
        print("Please login again.")
        if login() == True:
            while True:
                main_menu(acc.get_balanceobj())
        else:
            signup_or_login()
    elif choice == 'b':
        if login() == True:
            while True:
                main_menu(acc.get_balanceobj())
        else:
            signup_or_login()
        

signup_or_login()
