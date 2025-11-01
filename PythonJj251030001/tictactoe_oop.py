ALL_SPACES = list("123456789")
X, O, BLANK = "X", "O", " "
import copy


class TTTBoard:
    def __init__(self, usePrettyBoard=False, useLogging=False):
        self._spaces = {}
        for space in ALL_SPACES:
            self._spaces[space] = BLANK

    def getBoardStr(self):
        return f"""
        {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']} 1 2 3
        -+-+-
        {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']} 4 5 6
        -+-+-
        {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']} 7 8 9"""

    def isValidSpace(self, space):
        return space in ALL_SPACES and self._spaces[space] == BLANK

    def isWinner(self, player):
        b, p = self._spaces, player
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

    def isBoardFull(self):
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False
        return True

    def updateBoard(self, space, mark):
        self._spaces[space] = mark


class MiniBoard(TTTBoard):
    def getBoardStr(self):
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                self._spaces[space] = "."
        boardStr = f"""
        {self._spaces['1']}{self._spaces['2']}{self._spaces['3']} 123
        {self._spaces['4']}{self._spaces['5']}{self._spaces['6']} 456
        {self._spaces['7']}{self._spaces['8']}{self._spaces['9']} 789"""
        for space in ALL_SPACES:
            if self._spaces[space] == ".":
                self._spaces[space] = BLANK
        return boardStr


class HintBoard(TTTBoard):
    def getBoardStr(self):
        boardStr = super().getBoardStr()

        xCanWin = False
        oCanWin = False
        originalSpaces = self._spaces
        for space in ALL_SPACES:
            self._spaces = copy.copy(originalSpaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = X
            if self.isWinner(X):
                xCanWin = True
            self._spaces = copy.copy(originalSpaces)
            if self._spaces[space] == BLANK:
                self._spaces[space] = O
            if self.isWinner(O):
                oCanWin = True
        if xCanWin:
            boardStr += "\nX can win in one more move."
        if oCanWin:
            boardStr += "\nO can win in one more move."
        self._spaces = originalSpaces
        return boardStr


class HybridBoard(HintBoard, MiniBoard):
    pass

# class HybridBoard(MiniBoard, HintBoard):
#     pass

def main():
    print("Welcome to tic-tac-toe!")
    # if input("use mini board? Y/N: ").lower().startswith("y"):
    #     gameBoard = MiniBoard()
    # else:
    #     gameBoard = TTTBoard()

    gameBoard = HybridBoard()
    currentPlayer, nextPlayer = X, O

    while True:
        print(gameBoard.getBoardStr())

        move = None
        while not gameBoard.isValidSpace(move):
            print(f"what is {currentPlayer}'s move? (1-9)")
            move = input()
        gameBoard.updateBoard(move, currentPlayer)

        if gameBoard.isWinner(currentPlayer):
            print(gameBoard.getBoardStr())
            print(currentPlayer + " has won the game!")
            break
        elif gameBoard.isBoardFull():
            print(gameBoard.getBoardStr())
            print("the game is a tie!")
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print("Thanks for playing")


if __name__ == "__main__":
    main()
