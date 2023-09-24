from Board import board
from Person import person

board1 = board()
print("welcome to the 3D tic-tac-toe game")
name = input("please enter the first player's name: ")
firstPlayer = person(0, "X", name)
name = input("please enter the second player's name: ")
secondPlayer = person(0, "O", name)
print(f"Hello {firstPlayer.name} and {secondPlayer.name}, let's play the game")
flag = True
# currentplayer = random player
while flag:
    if not (currentplayer.playfun(board1)):
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