from inventory import *
import csv
from mainmenu import *

class Account:

    def __init__(self, user, password, balance):
        self.username = user
        self.password = password
        self.balance = Inventory(balance)

    def add_username(self, user):
        #sets username
        self.username = user

    def add_password(self, password):
        #sets password
        self.password = password

    def get_username(self):
        #returns username
        return self.username

    def get_password(self):
        #returns password
        return self.password
    
    def get_balance(self):
        #returns balance
        return self.balance.check_value()

    def get_balanceobj(self):
        #returns balance class instance
        return self.balance

    def __str__(self):
        return self.username

#function to create an account
def signup(): 
    user = input("Username: ")
    while len(user) < 3 or len(user) > 20 or user.replace('_', '').isalnum() == False: #rejects nonalphanumeric usernames
        user = input("Please choose a username that is 3 to 20 characters long,\nwith alphanumeric characters and underscores only:\n")
    password = input("Password: ")
    while len(password) < 6:
        password = input("Please choose a password that is at least 6 characters long:\n")
    with open("database.txt") as database:
        database_csv = csv.reader(database, delimiter=',')
        for line in database_csv: #iterates through database to check for existing username
            if user.lower() == line[0].lower():
                print("That username is already taken!")
                signup_or_login()
    global acc
    acc = Account(user, password, 500) #sets the account to start with 500 chips
    with open("database.txt", mode='a') as database: #adds account to database
        database.write(f"{acc.get_username()},{acc.get_password()},{acc.get_balance()}\n")

#function to login to existing account
def login():
    global user_input
    user_input = input("Username: ")
    password_input = input("Password: ")
    with open("database.txt") as database:
        database_csv = csv.reader(database, delimiter=',')
        for line in database_csv: #iterates through database to find account
            if user_input.lower() == line[0].lower():
                if password_input == line[1]: #check if username and password are correct
                    global acc
                    acc = Account(user_input, password_input, float(line[2])) #retrieves account information
                    return True
        print("Username or password is incorrect.")
        return False

#menu for user to choose to signup or login
def signup_or_login():
    print("(a) Sign up")
    print("(b) Login")
    choice = input("What would you like to do?\n")
    while choice not in ['a', 'b']: #rejects input if not in list
        choice = input("Invalid option, please try again: ")
    if choice == 'a':
        signup()
        print("Please login again.")
        if login() == True:
            while True:
                main_menu(user_input, acc.get_balanceobj())
        else:
            signup_or_login() #returns to menu if login is unsuccessful
    elif choice == 'b':
        if login() == True:
            while True:
                main_menu(user_input, acc.get_balanceobj())
        else:
            signup_or_login() #returns to menu if login is unsuccessful
