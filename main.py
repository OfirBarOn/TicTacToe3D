import random
from Board import board
from Person import person

board1 = board()

print("welcome to the 3D tic-tac-toe game")
name = input("please enter the first player's name: ")
firstPlayer = person(0, "X", name)
name = input("please enter the second player's name: ")
secondPlayer = person(0, "O", name)
print(f"Hello {firstPlayer.name} and {secondPlayer.name}, let's play the game")

current_player = random.choice(['X', 'O'])
if current_player == 'X':
    First_player_move = True
else:
    First_player_move = False

flag = True
first = False
second = False
while flag:
    if First_player_move:
        first = firstPlayer.playfun(board1)
        First_player_move = False

    if not First_player_move:
        second = secondPlayer.playfun(board1)
        First_player_move = True

    if not (first or second):
        continue
    else:
        while True:
            answer = input("Do you want to play another round? (y/n): ")
            if answer == 'y':
                flag = True
                board1 = board()
                break
            elif answer == 'n':
                flag = False
                break
            else:
                print("Invalid input")

        # if current_player == firstPlayer:
        #   Currentplayer = secondPlayer
        # else:
        #   Currentplayer = firstPlayer
