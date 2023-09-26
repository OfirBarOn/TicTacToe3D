import random
from inputimeout import inputimeout, TimeoutOccurred

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


    def check_full(self):
        for layer in range (3):
            for row in range(3):
                for column in range(3):
                    if (self.board[layer][row][column] == " "):
                        return False
        return True


    def check_win(self, player):
        # Check wins in each layer
        for layer in range(3):
            # Check horizontal and vertical in the same layer
            for i in range(3):
                if all(self.board[layer][i][j] == player for j in range(3)):
                    return True
                    # Check columns
                if all(self.board[layer][j][i] == player for j in range(3)):
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


    def validlayColRow(self):
        while True:
            try:
                #waits 60 seconds for input
                place = inputimeout(prompt="where do you want to add your move?", timeout=30)
                layer, row, column = map(int, place.split())
                if self.validate(row) and self.validate(column) and self.validate(layer):
                    place = [layer,row,column]
                    return place
                else:
                    print("Invalid Input")

            except TimeoutOccurred:
                print("You run out of time, It's the other player's turn")
                return None
            except (ValueError, IndexError):
                print("Invalid Input")

        return None


    def computerturn(self, shape):
    
        for layer in range(3):
            for row in range(3):
                for column in range(3):
                    if (self.board[layer][row][column] == " "):
                        self.board[layer][row][column] = shape
                        res = self.check_win(shape)
                        if res :
                            return 
                        self.board[layer][row][column] = " "
                        
        second_shape = "X" if shape == "O" else "O"
                        
        for layer in range(3):
            for row in range(3):
                for column in range(3):
                    if (self.board[layer][row][column] == " "):
                        self.board[layer][row][column] = second_shape
                        res = self.check_win(second_shape)
                        if res :
                            self.board[layer][row][column] = shape
                            return 
                        self.board[layer][row][column] = " "
        while True:
            layer = random.randrange(0, 3)
            row = random.randrange(0, 3)
            column = random.randrange(0, 3)
            if (self.board[layer][row][column] == " "):
                self.board[layer][row][column] = shape
                return
            
            


    def add_move(self, shape):
        while True:
            place = self.validlayColRow()
            if place == None:
                return
            layer =place[0] -1
            row = place[1] -1
            column =place[2] - 1
            #print(f'{layer} {row} {column}')
            if (self.board[layer][row][column] != " ") :
                print("This place is taken, pleace choose another place")
                self.add_move(shape)
            self.board[layer][row][column] = shape
            break
        return