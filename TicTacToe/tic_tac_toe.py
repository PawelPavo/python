#TicTacToe

from re import X
from secrets import choice


board=['#','X','O','X','O','X','O','X','O','X']

def display_board(board):
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])

#display_board(board)

def player_input():
    choice = input('Please enter X or O: ')
    while choice.upper() not in ['X','O']:
        print(f'{choice} is not a valid choice!')
        choice = input('Please enter X or O: ')

#player_input()

def place_marker(board, marker, position):
    pass