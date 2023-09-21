class Board:
    """Defines the boards of the game"""

    def __init__(self):
        self.board = [[[None] * 3 for i in range(3)] for i in range(3)]

    def display(self):
        print(self.board)  # - --> ['x', 'o', 'x'][none, 'x', none][....][....][....]

    def check_win(self, indexes):
        ...

    def add_move(self, shape):
        place = input("where do you want to add your move? (add three numbers level ,row ,column): ")
        separators = " ,"
        indexes = place.split(separators)
        self.board[level][row][column] = shape
        self.check_win(indexes)
        self.display()
