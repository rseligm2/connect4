class Board:
    
    def __init__(self):
        spaces = []
        for i in range(0,7):
            spaces.append([0] * 6)
        self._spaces = spaces
        self._turn = 1
        self._lastTurn = []
        
    def __str__(self):
        out = ''
        for j in range(5, -1, -1):
            for i in range(0, 7):
                out += str(self._spaces[i][j]) + ' '
            out += '\n'
        return out
        
    def changeTurn(self):
        if self._turn == 1:
            self._turn = 2
        else:
            self._turn = 1
            
    def addPiece(self, column):
        for i in range(0, 6):
            if self._spaces[column][i] > 0:
                continue
            else:
                self._spaces[column][i] = self._turn
                self._lastTurn = [column, i]
                break
           
    def checkWin(self):
        inARow = 0
        for i in range(0, self._lastTurn[1] + 1): #check for vertical win
            if self._spaces[self._lastTurn[0]][i] == self._turn:
                inARow += 1
            else:
                inARow = 0
            if inARow >= 4:
                return self._turn
        inARow = 0
        up = 0
        down = 0
        left = max(0, self._lastTurn[0] - 3)
        right = min(7, self._lastTurn[0] + 4)
        bottom = max(0, self._lastTurn[1] - 3)
        top = min(6, self._lastTurn[1] + 3)
        for i in range(left, right): #check for horizontal win
            if self._spaces[i][self._lastTurn[1]] == self._turn:
                inARow += 1
            else:
                inARow = 0
            if inARow >= 4:
                return self._turn
        for i, j in zip(range(left, right), range(bottom, top)): #check for diagonal up win
            if self._spaces[i][j] == self._turn:
                up += 1
            else:
                up = 0
            if up >= 4:
                return self._turn
        top = self._lastTurn[1]
        for i, j in zip(range(left, right), range(top, bottom - 1, -1)): #check for diagonal down win
            if self._spaces[i][j] == self._turn:
                down += 1
            else:
                down = 0
            if down >= 4:
                return self._turn
        return 0

def startGame():
    board = Board()
    while(True):
        print(board)
        print("Player " + str(board._turn) + ", it is your turn")
        col = input("Enter a column number: ")
        if not col.isdigit():
            print("Invalid, enter an integer")
            continue
        col = int(col)
        if col < 1 or col > 7:
            print("Invalid column")
            continue
        board.addPiece(col - 1)
        if board.checkWin() != 0:
            print(board)
            print("Player " + str(board._turn) + " wins!")
            break
        else:
            board.changeTurn()

def testDiagonalDownWin():
    board = Board()
    board.addPiece(3)
    board.changeTurn()
    board.addPiece(2)
    board.changeTurn()
    board.addPiece(2)
    board.changeTurn()
    board.addPiece(1)
    board.addPiece(1)
    board.changeTurn()
    board.addPiece(1)
    board.changeTurn()
    board.addPiece(0)
    board.addPiece(0)
    board.addPiece(0)
    board.changeTurn()
    board.addPiece(0)
    if board.checkWin() == 1:
        print("DiagonalDownWin Success")
    else:
        print("DiagonalDownWinError")

def testHorizontalWin():
    board = Board()
    board.addPiece(0)
    board.addPiece(1)
    board.addPiece(2)
    board.addPiece(3)
    if board.checkWin() == 1:
        print("HorizontalWin Success")
    else:
        print("HorizontalWinError")

def testDiagonalUpWin():
    board = Board()
    board.addPiece(0)
    board.changeTurn()
    board.addPiece(1)
    board.changeTurn()
    board.addPiece(1)
    board.changeTurn()
    board.addPiece(2)
    board.addPiece(2)
    board.changeTurn()
    board.addPiece(2)
    board.changeTurn()
    board.addPiece(3)
    board.addPiece(3)
    board.addPiece(3)
    board.changeTurn()
    board.addPiece(3)
    if board.checkWin() == 1:
        print("DiagonalUpWin Success")
    else:
        print("DiagonalUpWinError")

def testVerticalWin():
    board = Board()
    board.addPiece(0)
    board.addPiece(0)
    board.addPiece(0)
    board.addPiece(0)
    if board.checkWin() == 1:
        print("VerticalWin Success")
    else:
        print("VerticalWinError")

startGame()