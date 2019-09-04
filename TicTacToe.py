winConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

def play():
    board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    player = "X"  # "O"
    while winner(board) == None and ("_" in board):
        display_board(board)
        print("Current Player : " + player)
        idx = int(input("Please place piece at position:\n"))
        if board[idx] == "_":
            board[idx] = player
            player = reversePlayer(player)
    display_board(board)
    if winner(board) != None:
        print("Winner is " + winner(board))


def reversePlayer(player):
    if player == "X":
        return "O"
    else:
        return "X"


def winner(board):
    for indexes in winConditions:
        sequence = ""
        for idx in indexes:
            sequence += board[idx]
        if sequence == "XXX":
            return "X"
        elif sequence == "OOO":
            return "O"
    return None


def display_board(board):
    rows = ["", "", ""]
    for idx, piece in enumerate(board):
        rows[int(idx / 3)] += piece
    for row in rows:
        print(row)
    print("----------------------")


play()
