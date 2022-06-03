def check_winner(board,marker):
    return((board[1]==marker and board[2]== marker and board[3]==marker )or #for row1 

            (board[4]==marker and board[5]==marker and board[6]==marker )or #for row2

            (board[7]==marker and board[8]==marker and board[9]==marker )or #for row3

            (board[1]==marker and board[4]==marker and board[7]== marker )or#for Colm1 

            (board[2]==marker and board[5]==marker and board[8]==marker )or #for Colm 2

            (board[3]==marker and board[6]==marker and board[9]==marker )or #for colm 3

            (board[1]==marker and board[5]==marker and board[9]==marker )or #daignole 1

            (board[3]==marker and board[5]==marker and board[7]==marker )) #daignole 2
