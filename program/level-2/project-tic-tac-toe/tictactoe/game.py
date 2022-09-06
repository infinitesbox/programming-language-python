from tictactoe.board import *

def game_play():

    board = board_create()

    is_finished = False

    board_show(board)

    while (is_finished != True):
        
        row = input('Choose the row:') # give a string 
        row = int(row) # convert string to integer 

        column = input('Choose the column:') # give a string
        column = int(column) # convert string to integer

        token = board_get_token(board)

        try:
            # can make an Exception
            index = board_get_index_from_position(row, column)
        except:
            continue
        
        try:
            # can make an Exception
            board_put_token(board, index, token)
        except:
            continue

        board_show(board)

        has_winner, winner_token = board_has_winner(board)

        if(has_winner == True):
            print('We have a winner!')
            print('Winner: ', winner_token)
            print('Win in ', board['rounds'], ' rounds!')
            break

        is_finished = board_next_round(board)
        if(is_finished ==  True):
            print('No Winner - Game Over!')
            break
