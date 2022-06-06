from random import choice

print('Welcome to Tic Tac Toe?')
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
turn=0
play = True

def play():
    play_question=position = input('Do you want to play again? Type Y or N: ')
    if play_question=='Y':
        play=True
    else:
        print('Thanks, see you later!')
        

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
  
def space_check(board, position):
    if board[position]=='X' or board[position]=='O':
        return True
        

def win_check(board,marker):
    if board[0]=='X' and board[1]=='X' and board[2]=='X' or\
       board[3]=='X' and board[4]=='X' and board[5]=='X' or\
       board[6]=='X' and board[7]=='X' and board[8]=='X' or\
       board[0]=='X' and board[3]=='X' and board[6]=='X' or\
       board[1]=='X' and board[3]=='4' and board[7]=='X' or\
       board[2]=='X' and board[5]=='4' and board[8]=='X' or\
       board[0]=='X' and board[4]=='4' and board[8]=='X' or\
       board[2]=='X' and board[4]=='4' and board[6]=='X':
           print('X is the winner')
           play()
    if board[0]=='O' and board[1]=='O' and board[2]=='O' or\
       board[3]=='O' and board[4]=='O' and board[5]=='O' or\
       board[6]=='O' and board[7]=='O' and board[8]=='O' or\
       board[0]=='O' and board[3]=='O' and board[6]=='O' or\
       board[1]=='O' and board[3]=='O' and board[7]=='O' or\
       board[2]=='O' and board[5]=='O' and board[8]=='O' or\
       board[0]=='O' and board[4]=='O' and board[8]=='O' or\
       board[2]=='O' and board[4]=='O' and board[6]=='O':
           print('O is the winner')
           play()

def full_board_check(board):
    for space in board:
        if space == ' ':
            return False
    return True
    

while not full_board_check(board):
    position=position_choice()
    if space_check(board,position):
        print('Sorry, this position is taken.')
    else:
        place_marker(board,marker,position)
    if win_check(board,marker)== True or turn==9:
        if turn ==9:
            print('DRAW!')
            play()
        break
