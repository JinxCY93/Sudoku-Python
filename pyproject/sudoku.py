def split(sudoku):
    return [char for char in sudoku]

board = []
# for x in range(9):
# board.append([])
sudoku = "105802000090076405200400819019007306762083090000061050007600030430020501600308900"
# board.append(split(sudoku))
# print(split(sudoku[0:9]))
board.append(split(sudoku[0:9]))
board.append(split(sudoku[9:18]))
board.append(split(sudoku[18:27]))
board.append(split(sudoku[27:36]))
board.append(split(sudoku[36:45]))
board.append(split(sudoku[45:54]))
board.append(split(sudoku[54:63]))
board.append(split(sudoku[63:72]))
board.append(split(sudoku[72:81]))
print(board)

# def sublists(board):
#     board2 = []
#     for item in board:
#         for x in range(8):
#             if len(item[x])>9:
#                 if board2:
#                     yield board2
#                 board2 = []
#             else:
#                 board2.append(item)
#         if board2:
#             yield board2

# new_board = list(sublists(board))
# print(new_board)

# board = [
#     ["","","","","","","","",""],
#     ["","","","","","","","",""],
#     ["","","","","","","","",""],
#     ["","","","","","","","",""],
#     ["","","","","","","","",""],
#     ["","","","","","","","",""],
#     ["","","","","","","","",""],
#     ["","","","","","","","",""],
#     ["","","","","","","","",""]
# ]

def displayBoard(board):
    for x in range(len(board)):
        if x % 3 == 0 and x != 0:
            print("--------------------------")
    
        for y in range(len(board[0])):
            if y % 3 == 0 and y != 0:
                print(" | ", end ="")
        
            if y == 8:
                print(board[x][y])
            else:
                print (str(board[x][y]) + " " , end = "")

def checkRow(board, num, pos):
    for x in range(len(board[0])):
        if board[pos[0]][x] == num and pos[1] != x:
            return False
    return True

def checkCol(board, num, pos):
    for y in range(len(board)):
        if board[y][pos[1]] == num and pos[0] != y:
            return False
    return True

def checkBox(board, num, pos):
    box_x = pos[1] / 3
    box_y = pos[0] / 3

    for x in range(box_y*3, box_y*3 + 3 ):
        for y in range(box_x * 3, box_x * 3 + 3 ):
            if board[x][y] == num and (i,j) != pos:
                return False
    return True

def checkEmpty(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 0:
                return(x,y)
    return None

def solve(board):
    checkedBoard = checkEmpty(board)
    if not checkedBoard:
        return True
    else:
        row, col = checkedBoard

    for x in range(1,10):
        if checkRow(board, x, (row, col)):
            board[row][col] = x
            if solve(board):
                return True
            
            board[row][col] = 0

    for y in range(1,10):
        if checkCol(board, y, (row, col)):
            board[row][col] = y
            if solve(board):
                return True
            
            board[row][col] = 0

    for b in range(1,10):
        if checkBox(board, b, (row, col)):
            board[row][col] = b
            if solve(board):
                return True
            
            board[row][col] = 0

    return False

displayBoard(board)
solve(board)
print("_____________________________")
displayBoard(board)