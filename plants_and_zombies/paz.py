lawn = [
    '2       ',
    '  S     ',
    '21  S   ',
    '13      ',
    '2 3     '
]

zombies = [[0,4,28],[1,1,6],[2,0,10],[2,4,15],[3,2,16],[3,3,13]]


placeholder = '_'
move = 0
selected_row, selected_col = 0, 0


def create_board(lawn):
    board = [list(row) for row in lawn]
    for row in board:
        for i in range(len(row)):
            if row[i] == ' ':
                row[i] = placeholder

    return board


def print_board(board):
    print(f"step number {move}:")

    for row in board:
        for element in row:
            print(element, end=' ')
        print()
    print("\n")

def horizontal_shoot(shooter, board, row):
    global diff_damage

    if shooter == "S":
        hit = 1
    else:
        hit = int(shooter)
    if row < len(board):
        row = board[row]
        for index, element in enumerate(row):
            if isinstance(element, int):
                row[index] -= hit
                if row[index] <= 0: # < DISBALANCEEEE
                    row[index] = placeholder
                return
    else:
        print("Invalid row index.")

def diagonal_shoot(board, row, col):
    rows = len(board)
    cols = len(board[0])
    # print(board[row][col], end=" ")

    # down-right
    while row < rows - 1 and col < cols - 1:
        row += 1
        col += 1
        # print(board[row][col], end=" ")
        if isinstance(board[row][col], int):
            board[row][col] -= 1
            break

    # reset the values
    row = selected_row
    col = selected_col

    # up-right
    while row >= 0 and col < cols - 1:
        row -= 1
        col += 1
        # print(board[row][col], end=" ")
        if isinstance(board[row][col], int):
            board[row][col] -= 1
            break
    return



def plants_and_zombies(lawn, zombies):
    board = create_board(lawn)
    global move
    global selected_row, selected_col
    last_board = []

    while last_board != board:
        last_board = [row[:] for row in board]
        for row_index, row in enumerate(board):
            for col_index, element in enumerate(row):
                if isinstance(element, int): # if it is a zombie
                    if col_index > 0:
                        board[row_index][col_index], board[row_index][col_index - 1] = placeholder, board[row_index][col_index]
                    else:
                        print(f"Zommbies won!\nOn {move} move.\n")
                        return
                elif isinstance(element, str) and element != placeholder:
                    if element != "S": #if it is a num_shooter
                        if horizontal_shoot(element, board, board.index(row)) != None:
                            horizontal_shoot(element, board, board.index(row))
                    else: # if it is a S_shooter
                        if horizontal_shoot(element, board, board.index(row)) != None:
                            horizontal_shoot(element, board, board.index(row))
                        selected_row, selected_col = row_index, col_index
                        diagonal_shoot(board, row_index, col_index)

        for zombie in zombies:
            i = zombie[0]
            row = zombie[1]
            hp = zombie[2]
            if i == move:
                board[row][-1] = hp
                
        # print(board)
        print_board(board)
        
        move += 1
    else:
        print(f"Plants won!\nOn {move-1} move.\n")


plants_and_zombies(lawn,zombies)
