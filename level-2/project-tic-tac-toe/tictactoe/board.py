# Module Board

from cgi import print_arguments


def board_create():
    board = {
        'squares': ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
        'rounds': 1,
        'token': '-'
    }
    return board

def board_init(board, squares, rounds, token):
    board['squares'] = squares
    board['rounds'] = rounds
    board['token'] = token

def player_reset(board):
    board['name'] = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    board['rounds'] = 1
    board['token'] = '-'

def board_show(board):
    str = ''
    for index in range(len(board['squares'])):
        str = str + '[{0}]'.format(board['squares'][index])
        if((index + 1) % 3 == 0):
            str = str + '\n'   
    print(str)

def board_get_index_from_position(row, column):
    if(row > 3 or column > 3):
        print('Row and Column values must be less or equal than 3!')
        raise

    if(row < 1 or column < 1):
        print('Row and Column values must be more or equal than 1!')
        raise

    start_index = 0

    if(row == 2):
        start_index = 3
    if(row == 3):
        start_index = 6
    
    index = start_index + (column - 1)

    return index

def board_put_token(board, index, token):
    if(board['squares'][index] == '-'):
        board['squares'][index] = token
        board['token'] = token
    else:
        print('Have already a token!')
        raise
    return board

def board_has_winner(board):
    # rows
    if(board['squares'][0] != '-' and board['squares'][0] == board['squares'][1] and board['squares'][1] == board['squares'][2]):
        return (True, board['squares'][0])

    if(board['squares'][3] != '-' and board['squares'][3] == board['squares'][4] and board['squares'][4] == board['squares'][5]):
        return (True, board['squares'][3])

    if(board['squares'][6] != '-' and board['squares'][6] == board['squares'][7] and board['squares'][7] == board['squares'][8]):
        return (True, board['squares'][6])

    # columns
    if(board['squares'][0] != '-' and board['squares'][0] == board['squares'][3] and board['squares'][3] == board['squares'][6]):
        return (True, board['squares'][0])

    if(board['squares'][1] != '-' and board['squares'][1] == board['squares'][4] and board['squares'][4] == board['squares'][7]):
        return (True, board['squares'][1])

    if(board['squares'][2] != '-' and board['squares'][2] == board['squares'][5] and board['squares'][5] == board['squares'][8]):
        return (True, board['squares'][2])

    # diagonals
    if(board['squares'][0] != '-' and board['squares'][0] == board['squares'][4] and board['squares'][4] == board['squares'][8]):
        return (True, board['squares'][0])

    if(board['squares'][2] != '-' and board['squares'][2] == board['squares'][4] and board['squares'][4] == board['squares'][6]):
        return (True, board['squares'][2])

    return (False, '-')

def board_next_round(board):
    board['rounds'] = board['rounds'] + 1

    # no more rounds, because no more squares available
    return board['rounds'] >= len(board['squares'])

def board_get_token(board):
    if(board['rounds'] % 2 != 0):
        return 'X'
    else:
        return 'O'