from random import randint

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
#board=[' ',' ','X',' ','X',' ','X',' ',' ']
P1=''
P2=''
current_player=0

def player_input():
    marker='WRONG'
    markers=['X','O']
    while marker.upper() not in markers:
        marker = input('Please enter X or O: ')
        if marker.upper() not in markers:
            print(f'Sorry, {marker} is not a valide choice!')
    return marker.upper()

marker=player_input()

def choose_first():
    current_player = randint(1, 2)
    print("Player {} will go first.".format(current_player))

choose_first()

def display_board(board):
    print(board[0]+'|'+ board[1]+'|'+ board[2])
    print('-----')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-----')
    print(board[6]+'|'+board[7]+'|'+board[8])

display_board(board)

def position_choice():
    
    # VARS
    position='WRONG'
    acceptable_range = range(0,10)
    within_range = False
    
    # TWO CONDITIONS TO CHECK - DIGIT or WITHIN_RANGE == False
    while position.isdigit()== False or within_range == False:
        position = input('Please enter the position for your marker: ')
        # Digit Check
        if position.isdigit()==False:
            print(f'Sorry {position} is not a digit! Try again.')
            continue
        
        # range Check
        if position.isdigit()==True:
            if int(position) in acceptable_range:
                within_range=True
            else:
                within_range=False
                print('Please enter a valid position on the board!')
                continue
            
        return int(position)

def place_marker(board,marker,position):
    board[position-1] = marker
    display_board(board)

def space_check(board, position):
    if board[position-1]=='X' or board[position-1]=='O':
        print('Sorry, this position is taken.')

def full_board_check(board):
    for space in board:
        if space == ' ':
            return False
    return True

def win_check(board,marker):
    winner=[]
    win_combos={'combo1':[0,1,2],
                'combo2':[3,4,5],
                'combo3':[6,7,8],
                'combo4':[0,3,6],
                'combo5':[1,4,7],
                'combo6':[2,5,8],
                'combo7':[6,4,2],
                'combo8':[0,4,8]}
    for index,char in enumerate(board):
        if char == marker:
            winner.append(index)
            for win in win_combos.values():
                if winner == win:
                    print(f'{marker} is the winner!')
                    return True

while not full_board_check(board):
    position=position_choice()
    space_check(board,position)
    place_marker(board,marker,position)
    if win_check(board,marker)== True:
        break

















