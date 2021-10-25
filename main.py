#main
from board import Board

def main():
    rows = int(input('Hoeveel rijen? '))
    colums = int(input('Hoeveel colommen? '))

    board = Board(rows,colums)
    board.drawBoard()

    i = 0 
    inputs = ''
    while inputs != 'q':
        inputs = ''
        i = i+1
        if inputs == '':
            board.updateBoard()
            board.drawBoard()
        if i == 1:
            inputs = input('Enter voor next generation, q om te stoppah')
            i = 0
main()