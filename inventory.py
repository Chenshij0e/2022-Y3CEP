class Inventory:
    def __init__(self, value):
        self.value = value

    def add_value(self, adding):
        #adds to balance
        self.value += adding

    def place_bet(self, bet):
        #removes from balance
        self.value -= bet

    def check_value(self):
        #returns balance
        return self.value

    def __str__(self):
        return self.value
