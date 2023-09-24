from board import board
class person:
    def __init__(self, number_of_winnings, shape, name):
        self.number_of_winnings = number_of_winnings
        self.name = name
        self.shape = shape

    def __str__(self):
        return self.name

    def playfun(self, board):
        if self.name == 'computer':
            print("it's the computers turn")
            board.computerturn(self.shape)
        else:
            print(f"{self} it's your turn.")
            board.add_move(self.shape)
        board.display()
        if board.check_win(self.shape):
            self.number_of_winnings += 1
            if self != 'computer':
                print(f'congratulations {self} you won!')
                print(f'you have won {self.number_of_winnings} time(s)!')
            else:
                print("I'm sorry You lost")
                print(f'The computer have won {self.number_of_winnings} time(s)!')
            return True
        return False
