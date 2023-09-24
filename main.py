import random
from board import board
from person import person

board1 = board()

print("welcome to the 3D tic-tac-toe game")
while True:
    answer = input("Do you want to play with a computer? (y/n): ")
    if answer != 'y' and answer != 'n':
        print("Invalid input, please try again!")
    else:
        break

if answer == 'y':
    name = input("please enter your name: ")
    firstPlayer = person(0, "X", name)
    secondPlayer = person(0, "O", 'computer')
    print(f"Hello {firstPlayer.name}, let's play the game")
else:
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
while flag:
    if First_player_move:
        First_player_move = False
        if not firstPlayer.playfun(board1):
            continue

    else:
        First_player_move = True
        if not secondPlayer.playfun(board1):
            continue

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
