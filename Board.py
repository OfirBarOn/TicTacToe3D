class board:
    def __init__(self):
        self.board = [[[" "] * 3 for i in range(3)] for i in range(3)]

    def display(self):
        for layer in range (3):
            for row in range(3):
                print("|", end="")
                for column in range(3):
                    print(self.board[layer][row][column] , end="|")
                print("")
            print("*******")
        return

    def check_win(self, player):
        # Check wins in each layer
        for layer in range(3):
            # Check horizontal and vertical in the same layer
            for i in range(3):
                if all(self.board[i][j] == player for j in range(3)):
                    return True
                    # Check columns
                if all(self.board[j][i] == player for j in range(3)):
                    return True
            # Check diagonals in the current layer
            if all(self.board[layer][i][i] == player for i in range(3)):
                return True
            if all(self.board[layer][i][2 - i] == player for i in range(3)):
                return True

        # Check wins that span across layers
        for i in range(3):
            # Check rows and columns that span across layers
            for j in range(3):
                if all(self.board[layer][i][j] == player for layer in range(3)):
                        return True
        # Check win diagonals that span across layer
        for i in range(3):
            if all(self.board[j][i][j] == player for j in range(3)):
                return True
            if all(self.board[j][i][2-j] == player for j in range(3)):
                return True
            if all(self.board[j][j][i] == player for j in range(3)):
                return True
            if all(self.board[j][2-j][i] == player for j in range(3)):
                return True

        # Check win in 4 big Dagonals
        if all(self.board[i][i][i] == player for i in range(3)):
            return True
        if all(self.board[i][i][2-i] == player for i in range(3)):
            return True
        if all(self.board[i][2-i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2-i][2-i] == player for i in range(3)):
            return True
        return False

    def validate(self, num):
        try:
            if 1 <= num <= 3:
                return True
            else:
                return False
        except ValueError:
            return False

    def add_move(self, shape):
        layer = int(input("In which layer do you want to play?: "))
        while not self.validate(layer):
            layer = int(input("Invalid input, please enter a number Between 1, 2, 3: "))
        layer -= 1
        place = input("where do you want to add your move?"
                      "(add two numbers row and column seperated with space): ")
        while True:
            try:
                row, column = map(int, place.split())
                if self.validate(row) and self.validate(column):
                    break
                else:
                    print("Invalid Input")
            except (ValueError, IndexError):
                print("Invalid Input")
            place = input("where do you want to add your move?"
                          "(add two numbers row and column seperated with space): ")

        row -= 1
        column -= 1
        if (board[layer][row][column] != " ") :
            print("This place is taken, pleace choose another place")
            self.add_move(shape)
        self.board[layer][row][column] = shape
        self.display()
        return  self.check_win(shape)
