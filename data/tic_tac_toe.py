def get_move(board):  #t akes input from player and turns it into valid coordinates. Checks for coordinates already taken on the board
    cor_1 = 0
    cor_2 = 0
    while True:
        move = input("Provide coordinates (A-C for rows, 1-3 for columns. Example - 'C2'): ").lower()
        if len(move) != 2 or move[0] not in ("a", "b", "c") or move[1] not in ("1","2","3"):
            print("This is not valid")
            continue
        else:
            if move[0] == "a":
                cor_1 = 0
            if move[0] == "b":
                cor_1 = 1
            if move[0] == "c":
                cor_1 = 2
            cor_2 = int(move[1]) - 1
            if board[cor_1][cor_2] != ".":
                print(f"{move.upper()} already taken")
                continue
            elif board[cor_1][cor_2] == ".":
                break
        
    return (cor_1, cor_2)

# def get_move_computer(board):  # NOT FINISHED processes the board situation and choose computer move
#     cor_1 = 0
#     cor_2 = 0
#     return (cor_1, cor_2)

def mark(board, player, coordinates):  # returns board updated with new move
    marked_board = board
    marked_board[coordinates[0]][coordinates[1]] = player
    return marked_board

def display_board(board):  # prints current board
    print(f"""\n   1 2 3\n\nA |{board[0][0]}|{board[0][1]}|{board[0][2]}|\nB |{board[1][0]}|{board[1][1]}|{board[1][2]}|\nC |{board[2][0]}|{board[2][1]}|{board[2][2]}|""")

def win_lose(board, player):  # determines current board situation and decides if the game is finished or still being played
    if board[0][0] + board[0][1] + board[0][2] == player * 3 or board[1][0] + board[1][1] + board[1][2] == player * 3 or board[2][0] + board[2][1] + board[2][2] == player * 3 or board[0][0] + board[1][0] + board[2][0] == player * 3 or board[0][1] + board[1][1] + board[2][1] == player * 3 or board[0][2] + board[1][2] + board[2][2] == player * 3 or board[0][0] + board[1][1] + board[2][2] == player * 3 or board[2][0] + board[1][1] + board[0][2] == player * 3:
        return [1, player + " wins"]
    elif "." not in "".join(board[0]) + "".join(board[1]) + "".join(board[2]):
        return [1, "draw"]
    else:
        return [0]

def main_multiplayer():  # use for player vs player
    board = [[".",".","."],[".",".","."],[".",".","."]]
    player = ["X", "O", 0]
    print("Welcome to Tic Tac Toe\nX starts the game")
    while True:
        board = mark(board, player[player[2] % 2], get_move(board))
        display_board(board)
        if win_lose(board, player[player[2] % 2])[0] == 1:
            print(win_lose(board, player[player[2] % 2])[1])
            replay = input("Want to play again? ").lower()
            if replay[0] == "y":
                board = [[".",".","."],[".",".","."],[".",".","."]]
            else:
                print("You have not selected 'yes'. Closing the game.")
                break
        player[2] += 1
    print("Bye")

def main_singleplayer():  # NOT FINISHED use for player vs computer
    board = [[".",".","."],[".",".","."],[".",".","."]]
    player = ["X", "O", 0]
    print("Welcome to Tic Tac Toe\nPlayer starts the game as X")
    while True:
        if player[2] == 0:
            board = mark(board, player[player[2] % 2], get_move(board))
            display_board(board)
        elif player[2] == 1:
            board = mark(board, player[player[2] % 2], get_move_computer(board))
            display_board(board)     
        if win_lose(board, player[player[2] % 2])[0] == 1:
            print(win_lose(board, player[player[2] % 2])[1])
            replay = input("Want to play again? ").lower()
            if replay[0] == "y":
                board = [[".",".","."],[".",".","."],[".",".","."]]
            else:
                print("You have not selected 'yes'. Closing the game.")
                break
        player[2] += 1
    print("Bye")

main_multiplayer()