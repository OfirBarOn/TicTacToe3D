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
        if not firstPlayer.playfun(board1):
            First_player_move = False
            continue

    else:
        if not secondPlayer.playfun(board1):
            First_player_move = True
            continue
    if First_player_move:
        winner = firstPlayer
    else:
        winner = secondPlayer
    if winner.name == 'computer':
        print("Sorry you Lost!")
    else:    
        print(f'congratulations {winner} you won!')
    print(f'The score is {firstPlayer} : {firstPlayer.number_of_winnings} , {secondPlayer} : {secondPlayer.number_of_winnings}')
    
    current_player = random.choice(['X', 'O'])
    if current_player == 'X':
        First_player_move = True
    else:
        First_player_move = False
        
        
    while True:
        answer = input("Do you want to play another round? (y/n): ")
        if answer == 'y':
            flag = True
            board1 = board()
            break
        elif answer == 'n':
            print("It was Fun ^_^, GoodBye!")
            flag = False
            break
        else:
            print("Invalid input")
