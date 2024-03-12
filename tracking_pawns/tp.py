import re

pawn_color = {-1:"W", 1:"B"}
# pawn_color = {-1:"P", 1:"p"}


def is_valid_move(move):
    pattern_move = r'^[a-h][1-8]$'
    pattern_capture = r'^[a-h]x[a-h][1-8]$'

    return re.match(pattern_move, move) is not None or re.search(pattern_capture, move) is not None

def create_board():
    board = [["."]*8 for _ in range(8)]

    for i in range(8):
        board[1][i] = pawn_color[1]

    for i in range(8):
        board[-2][i] = pawn_color[-1]

    # board[0][0] = "x" # for orientation
    # board[-1][7] = "y"
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))
    # print(board)
    print("\n")

def coor_to_index(coord):
    col = ord(coord[0])-ord('a')
    row = 8-int(coord[1]) 
    return (row,col)

def pawn_move_tracker(moves):
    board = create_board()
    print(moves)
    turn = -1
    stroke_number = 0
    for move in moves:
        stroke_number += 1
        print(f"- - - {stroke_number} - - - -")
        if is_valid_move(move):
            if(len(move)==2):
                row, col = coor_to_index(move[:2])
                if(board[row][col] != "."):
                    print(move + " is invalid\n")
                    return
                old_row = row-turn
                if(board[row-turn][col]=='.'):
                    if(((row-turn*2) in (1, 6)) and board[row-turn*2][col]!='.'):
                        old_row = row-turn*2
                    else:
                        print(move + " is invalid\n")
                        return            
                board[old_row][col] = "."
                board[row][col]=pawn_color[turn]
            elif(len(move)==4):
                row,col = coor_to_index(move[2:4])
                offset = ord(move[2])-ord(move[0])
                if(board[row][col] == "." or  board[row-turn][col-offset] == "."):
                    print(move + " is invalid\n")
                    return
                board[row-turn][col-offset] = "."
                board[row][col]=pawn_color[turn] = pawn_color[turn]                       
            turn = turn * -1
            print_board(board)
        else:
            print(move + " is incorrect input\n")
            return
            turn = turn * -1


# Tests
moves1 = ["c3"]
pawn_move_tracker(moves1)

moves2 = ["d4", "d5", "f3", "c6", "f4"]
pawn_move_tracker(moves2)

moves3 = ["d4", "d5", "f3", "c6", "f4", "c5", "dxc5"]
pawn_move_tracker(moves3)

moves4 = ["e6"]
pawn_move_tracker(moves4)

moves5 = ["e4", "d5", "exf5"]
pawn_move_tracker(moves5)

moves6 = ["e44", "d5"]
pawn_move_tracker(moves6)