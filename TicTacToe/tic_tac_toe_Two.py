from random import choice

print('Welcome to Tic Tac Toe?')
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
turn=0
def choose_first():
    player_1= choice([1,2])
    print("Player {} will go first.".format(player_1))
    return player_1

player_1=choose_first()

def choose_marker(player_1):
        marker='WRONG'
        markers=['X','O']
        while marker.upper() not in markers:
            marker = input('Please select X or O: ')
            if marker.upper() not in markers:
                print(f'Sorry, {marker} is not a valide choice!')
        if marker.upper() == 'X':
            player_1 = 'X'
            player_2 = 'O'
        else:
            player_1 = 'O'
            player_2 = 'X'
        return player_1,player_2


marker=list(choose_marker(player_1))

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
    global turn
    if turn%2==0:
        board[position] = marker[0]
    else:
        board[position] = marker[1]
    display_board(board)
    turn+=1
    print(turn)
  
def space_check(board, position):
    if board[position]=='X' or board[position]=='O':
        return True
        
def full_board_check(board):
    for space in board:
        if space == ' ':
            return False
    return True

def win_check(board,marker):
    return((board[1]==marker and board[2]== marker and board[3]==marker )or #for row1 

            (board[4]==marker and board[5]==marker and board[6]==marker )or #for row2

            (board[7]==marker and board[8]==marker and board[9]==marker )or #for row3

            (board[1]==marker and board[4]==marker and board[7]== marker )or#for Colm1 

            (board[2]==marker and board[5]==marker and board[8]==marker )or #for Colm 2

            (board[3]==marker and board[6]==marker and board[9]==marker )or #for colm 3

            (board[1]==marker and board[5]==marker and board[9]==marker )or #daignole 1

            (board[3]==marker and board[5]==marker and board[7]==marker )) #daignole 2


while not full_board_check(board):
    position=position_choice()
    if space_check(board,position):
        print('Sorry, this position is taken.')
    else:
        place_marker(board,marker,position)
    if win_check(board,marker)== True or turn==9:
        if turn ==9:
            print('DRAW!')            
        break
