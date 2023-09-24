from board import board

class person:
    def __init__(self, number_of_winnings, shape, name):
        self.number_of_winnings = number_of_winnings
        self.name = name
        self.shape = shape

    def __str__(self):
        return self.name

    def playfun(self, board):
        print(f"{self} it's your turn.")
        if board.add_move(self.shape):
            print(f'congratulations {self} you won!')
            self.number_of_winnings += 1
            return True
        return False
