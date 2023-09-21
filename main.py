from Person import Person
from Board import Board


def main():
    print('Welcome to our 3D Tic-Tac-Toe!')
    player1 = input('First player, Please enter your name: ')
    player2 = input('Second player, Please enter your name: ')
    p1 = Person(0, 'X', player1)
    p2 = Person(0, 'O', player2)
    print(p1.name)
    print(p2.name)

    Board.display()


if __name__ == '__main__':
    main()
