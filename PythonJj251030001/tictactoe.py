ALL_SPACES = list("123456789")
X, O, BLANK = "X", "O", " "


def getBlankBoard():
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK
    return board


def getBoardStr(board):
    return f"""
    {board['1']}|{board['2']}|{board['3']} 1 2 3
    -+-+-
    {board['4']}|{board['5']}|{board['6']} 4 5 6
    -+-+-
    {board['7']}|{board['8']}|{board['9']} 7 8 9"""


def isValidSpace(board, space):
    return space in ALL_SPACES and board[space] == BLANK


def isWinner(board, player):
    b, p = board, player
    return (
        (b["1"] == b["2"] == b["3"] == p)
        or (b["4"] == b["5"] == b["6"] == p)
        or (b["7"] == b["8"] == b["9"] == p)
        or (b["1"] == b["4"] == b["7"] == p)
        or (b["2"] == b["5"] == b["8"] == p)
        or (b["3"] == b["6"] == b["9"] == p)
        or (b["3"] == b["5"] == b["7"] == p)
        or (b["1"] == b["5"] == b["9"] == p)
    )


def isBoardFull(board):
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False
    return True


def updateBoard(board, space, mark):
    board[space] = mark


def main():
    print("Welcome to tic-tac-toe!")
    gameBoard = getBlankBoard()
    currentPlayer, nextPlayer = X, O

    while True:
        print(getBoardStr(gameBoard))

        move = None
        while not isValidSpace(gameBoard, move):
            print(f"what is {currentPlayer}'s move? (1-9)")
            move = input()
        updateBoard(gameBoard, move, currentPlayer)

        if isWinner(gameBoard, currentPlayer):
            print(getBoardStr(gameBoard))
            print(currentPlayer + " has won the game!")
            break
        elif isBoardFull(gameBoard):
            print(getBoardStr(gameBoard))
            print("the game is a tie!")
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print("Thanks for playing")


if __name__ == "__main__":
    main()
