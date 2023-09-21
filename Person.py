class Person:
    """Defines each person who plays the game at the moment"""
    def __init__(self, number_of_winnings, shape, name):
        self.number_of_winnings = number_of_winnings
        self.name = name
        self.shape = shape

    def __str__(self):
        return self.name
