class board:
    def __init__(self):
        self.board = [[[" "] * 3 for i in range(3)] for i in range(3)]

    def display(self):
        for layer in range(3):
            for row in range(3):
                print("|", end="")
                for column in range(3):
                    print(self.board[layer][row][column] , end="|")
                print("")
            print("*******")
        return

    def check_win(self, indexes):
        print("hello")
        return

    def add_move(self, shape):
        layer = int(input("In which layer do you want to play?: "))
        place = input("where do you want to add your move? (add two numbers row and column): ")
        separators = " "
        indexes = place.split(separators)
        row = int(indexes[0])
        column = int(indexes[1])
        self.board[layer][row][column] = shape
        self.check_win(indexes)
        self.display()