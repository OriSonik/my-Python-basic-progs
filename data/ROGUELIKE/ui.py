def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    w = len(board[1])
    h = len(board)

    print('='*(w+2))
    for row in range(h):
        print('|',end='')
        print(''.join(board[row]), sep = '', end = '')
        print('|')
    print('='*(w+2))
    print('\u001b[4mK E Y   B I N D I N G S :\u001b[0m       \u001b[2m[q] - quit\u001b[0m')
    print('\u001b[2m   [w]        for               [h] - help\u001b[0m')
    print('\u001b[2m[a][s][d] - movement       [i] - inventory\u001b[0m')
    print('')