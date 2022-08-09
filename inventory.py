class Inventory:
    def __init__(self, value):
        self.value = value

    def add_value(self, adding):
        self.value += adding

    def place_bet(self, bet):
        self.value -= bet

    def check_value(self):
        return self.value
