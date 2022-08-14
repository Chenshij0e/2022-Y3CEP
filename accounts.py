class Account:

    def __init__(self):
        self.username = ''
        self.password = ''

    def add_username(self, user):
        self.username = user

    def check_username(self, user_input):
        if self.username.lower() == user_input.lower():
            return True
        else:
            return False

    def add_password(self, password):
        self.password = password

    def check_password(self, password_input):
        if self.password == password_input:
            return True
        else:
            return False

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def __str__(self):
        return self.username

acc = Account()
def signup():
    user = input("Username: ")
    password = input("Password: ")
    while len(user) < 3 or len(user) > 20:
        user = input("Please choose a username between 3 and 20 characters long:\n")
        password = input("Password: ")
    if len(user) >= 3 and len(user) <= 20:
        acc.add_username(user)
        acc.add_password(password)


def login():
    user_input = input("Username: ")
    password_input = input("Password: ")
    while acc.check_username(user_input) == False or acc.check_password(password_input) == False:
        user_input = input("Invalid username or password, pls try again.\nUsername: ")
        password_input = input("Password: ")
    if acc.check_username(user_input) == True and acc.check_password(password_input) == True:
        return True    
            

def signup_or_login():
    
    print("a: Sign up")
    print("b: Login")
    choice = input("What would you like to do?\n")
    while choice not in ['a', 'b']:
        choice = input("Invalid option, pls try again: ")
    if choice == 'a':
        signup()
        login()
    elif choice == 'b' and acc.get_username() == '' and acc.get_password() == '':
        
