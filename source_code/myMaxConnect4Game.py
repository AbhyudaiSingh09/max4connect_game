
import random
import sys

class maxConnect4Game:
    def __init__(self):
        self.gameBoard = [[0 for i in range(7)] for j in range(6)]
        self.currentTurn = 1
        self.player1Score = 0
        self.player2Score = 0
        self.pieceCount = 0
        self.gameFile = None
        random.seed()

    def checkPieceCount(self):
        self.pieceCount = sum(1 for row in self.gameBoard for piece in row if piece)
    def printGameBoard(self):
        print (' -----------------')
        for i in range(6):
            print ('|')
            for j in range(7):
                print('%d' % self.gameBoard[i][j]),
            print ('| ')
        print (' -----------------')

    def printGameBoardToFile(self):
        for row in self.gameBoard:
            self.gameFile.write(''.join(str(col) for col in row) + '\r\n')
        self.gameFile.write('%s\r\n' % str(self.currentTurn))

    def playPiece(self, column):
        if not self.gameBoard[0][column]:
            for i in range(5, -1, -1):
                if not self.gameBoard[i][column]:
                    self.gameBoard[i][column] = self.currentTurn
                    self.pieceCount += 1
                    return 1


    def aiPlay(self,depth):
        bestScore= float('-inf')
        bestColumn = None
        for col in range(7):
            if self.playPiece(col):
                score = self.minimax(depth-1,float('-inf'),float('inf'),False)
                self.undoPlayPiece(col)

                if score> bestScore: 
                    bestScore = score
                    bestColumn = col 
        if bestColumn is not None: 
            self.playPiece(bestColumn)
            print('\n\nmove %d: Player %d, column %d\n' % (self.pieceCount, self.currentTurn, bestColumn+1))
            if self.currentTurn == 1:
                self.currentTurn = 2
            elif self.currentTurn == 2:
                self.currentTurn = 1

    def countScore(self):
            self.player1Score = 0
            self.player2Score = 0

            # Check horizontally
            for row in self.gameBoard:
                # Check player 1
                if row[0:4] == [1]*4:
                    self.player1Score += 1
                if row[1:5] == [1]*4:
                    self.player1Score += 1
                if row[2:6] == [1]*4:
                    self.player1Score += 1
                if row[3:7] == [1]*4:
                    self.player1Score += 1
                # Check player 2
                if row[0:4] == [2]*4:
                    self.player2Score += 1
                if row[1:5] == [2]*4:
                    self.player2Score += 1
                if row[2:6] == [2]*4:
                    self.player2Score += 1
                if row[3:7] == [2]*4:
                    self.player2Score += 1

            # Check vertically
            for j in range(7):
                # Check player 1
                if (self.gameBoard[0][j] == 1 and self.gameBoard[1][j] == 1 and
                    self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1):
                    self.player1Score += 1
                if (self.gameBoard[1][j] == 1 and self.gameBoard[2][j] == 1 and
                    self.gameBoard[3][j] == 1 and self.gameBoard[4][j] == 1):
                    self.player1Score += 1
                if (self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1 and
                    self.gameBoard[4][j] == 1 and self.gameBoard[5][j] == 1):
                    self.player1Score += 1
                # Check player 2
                if (self.gameBoard[0][j] == 2 and self.gameBoard[1][j] == 2 and
                    self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2):
                    self.player2Score += 1
                if (self.gameBoard[1][j] == 2 and self.gameBoard[2][j] == 2 and
                    self.gameBoard[3][j] == 2 and self.gameBoard[4][j] == 2):
                    self.player2Score += 1
                if (self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2 and
                    self.gameBoard[4][j] == 2 and self.gameBoard[5][j] == 2):
                    self.player2Score += 1

            # Check diagonally

            # Check player 1
            if (self.gameBoard[2][0] == 1 and self.gameBoard[3][1] == 1 and
                self.gameBoard[4][2] == 1 and self.gameBoard[5][3] == 1):
                self.player1Score += 1
            if (self.gameBoard[1][0] == 1 and self.gameBoard[2][1] == 1 and
                self.gameBoard[3][2] == 1 and self.gameBoard[4][3] == 1):
                self.player1Score += 1
            if (self.gameBoard[2][1] == 1 and self.gameBoard[3][2] == 1 and
                self.gameBoard[4][3] == 1 and self.gameBoard[5][4] == 1):
                self.player1Score += 1
            if (self.gameBoard[0][0] == 1 and self.gameBoard[1][1] == 1 and
                self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1):
                self.player1Score += 1
            if (self.gameBoard[1][1] == 1 and self.gameBoard[2][2] == 1 and
                self.gameBoard[3][3] == 1 and self.gameBoard[4][4] == 1):
                self.player1Score += 1
            if (self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1 and
                self.gameBoard[4][4] == 1 and self.gameBoard[5][5] == 1):
                self.player1Score += 1
            if (self.gameBoard[0][1] == 1 and self.gameBoard[1][2] == 1 and
                self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1):
                self.player1Score += 1
            if (self.gameBoard[1][2] == 1 and self.gameBoard[2][3] == 1 and
                self.gameBoard[3][4] == 1 and self.gameBoard[4][5] == 1):
                self.player1Score += 1
            if (self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1 and
                self.gameBoard[4][5] == 1 and self.gameBoard[5][6] == 1):
                self.player1Score += 1
            if (self.gameBoard[0][2] == 1 and self.gameBoard[1][3] == 1 and
                self.gameBoard[2][4] == 1 and self.gameBoard[3][5] == 1):
                self.player1Score += 1
            if (self.gameBoard[1][3] == 1 and self.gameBoard[2][4] == 1 and
                self.gameBoard[3][5] == 1 and self.gameBoard[4][6] == 1):
                self.player1Score += 1
            if (self.gameBoard[0][3] == 1 and self.gameBoard[1][4] == 1 and
                self.gameBoard[2][5] == 1 and self.gameBoard[3][6] == 1):
                self.player1Score += 1

            if (self.gameBoard[0][3] == 1 and self.gameBoard[1][2] == 1 and
                self.gameBoard[2][1] == 1 and self.gameBoard[3][0] == 1):
                self.player1Score += 1
            if (self.gameBoard[0][4] == 1 and self.gameBoard[1][3] == 1 and
                self.gameBoard[2][2] == 1 and self.gameBoard[3][1] == 1):
                self.player1Score += 1
            if (self.gameBoard[1][3] == 1 and self.gameBoard[2][2] == 1 and
                self.gameBoard[3][1] == 1 and self.gameBoard[4][0] == 1):
                self.player1Score += 1
            if (self.gameBoard[0][5] == 1 and self.gameBoard[1][4] == 1 and
                self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1):
                self.player1Score += 1
            if (self.gameBoard[1][4] == 1 and self.gameBoard[2][3] == 1 and
                self.gameBoard[3][2] == 1 and self.gameBoard[4][1] == 1):
                self.player1Score += 1
            if (self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1 and
                self.gameBoard[4][1] == 1 and self.gameBoard[5][0] == 1):
                self.player1Score += 1
            if (self.gameBoard[0][6] == 1 and self.gameBoard[1][5] == 1 and
                self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1):
                self.player1Score += 1
            if (self.gameBoard[1][5] == 1 and self.gameBoard[2][4] == 1 and
                self.gameBoard[3][3] == 1 and self.gameBoard[4][2] == 1):
                self.player1Score += 1
            if (self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1 and
                self.gameBoard[4][2] == 1 and self.gameBoard[5][1] == 1):
                self.player1Score += 1
            if (self.gameBoard[1][6] == 1 and self.gameBoard[2][5] == 1 and
                self.gameBoard[3][4] == 1 and self.gameBoard[4][3] == 1):
                self.player1Score += 1
            if (self.gameBoard[2][5] == 1 and self.gameBoard[3][4] == 1 and
                self.gameBoard[4][3] == 1 and self.gameBoard[5][2] == 1):
                self.player1Score += 1
            if (self.gameBoard[2][6] == 1 and self.gameBoard[3][5] == 1 and
                self.gameBoard[4][4] == 1 and self.gameBoard[5][3] == 1):
                self.player1Score += 1

            # Check player 2
            if (self.gameBoard[2][0] == 2 and self.gameBoard[3][1] == 2 and
                self.gameBoard[4][2] == 2 and self.gameBoard[5][3] == 2):
                self.player2Score += 1
            if (self.gameBoard[1][0] == 2 and self.gameBoard[2][1] == 2 and
                self.gameBoard[3][2] == 2 and self.gameBoard[4][3] == 2):
                self.player2Score += 1
            if (self.gameBoard[2][1] == 2 and self.gameBoard[3][2] == 2 and
                self.gameBoard[4][3] == 2 and self.gameBoard[5][4] == 2):
                self.player2Score += 1
            if (self.gameBoard[0][0] == 2 and self.gameBoard[1][1] == 2 and
                self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2):
                self.player2Score += 1
            if (self.gameBoard[1][1] == 2 and self.gameBoard[2][2] == 2 and
                self.gameBoard[3][3] == 2 and self.gameBoard[4][4] == 2):
                self.player2Score += 1
            if (self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2 and
                self.gameBoard[4][4] == 2 and self.gameBoard[5][5] == 2):
                self.player2Score += 1
            if (self.gameBoard[0][1] == 2 and self.gameBoard[1][2] == 2 and
                self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2):
                self.player2Score += 1
            if (self.gameBoard[1][2] == 2 and self.gameBoard[2][3] == 2 and
                self.gameBoard[3][4] == 2 and self.gameBoard[4][5] == 2):
                self.player2Score += 1
            if (self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2 and
                self.gameBoard[4][5] == 2 and self.gameBoard[5][6] == 2):
                self.player2Score += 1
            if (self.gameBoard[0][2] == 2 and self.gameBoard[1][3] == 2 and
                self.gameBoard[2][4] == 2 and self.gameBoard[3][5] == 2):
                self.player2Score += 1
            if (self.gameBoard[1][3] == 2 and self.gameBoard[2][4] == 2 and
                self.gameBoard[3][5] == 2 and self.gameBoard[4][6] == 2):
                self.player2Score += 1
            if (self.gameBoard[0][3] == 2 and self.gameBoard[1][4] == 2 and
                self.gameBoard[2][5] == 2 and self.gameBoard[3][6] == 2):
                self.player2Score += 1

            if (self.gameBoard[0][3] == 2 and self.gameBoard[1][2] == 2 and
                self.gameBoard[2][1] == 2 and self.gameBoard[3][0] == 2):
                self.player2Score += 1
            if (self.gameBoard[0][4] == 2 and self.gameBoard[1][3] == 2 and
                self.gameBoard[2][2] == 2 and self.gameBoard[3][1] == 2):
                self.player2Score += 1
            if (self.gameBoard[1][3] == 2 and self.gameBoard[2][2] == 2 and
                self.gameBoard[3][1] == 2 and self.gameBoard[4][0] == 2):
                self.player2Score += 1
            if (self.gameBoard[0][5] == 2 and self.gameBoard[1][4] == 2 and
                self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2):
                self.player2Score += 1
            if (self.gameBoard[1][4] == 2 and self.gameBoard[2][3] == 2 and
                self.gameBoard[3][2] == 2 and self.gameBoard[4][1] == 2):
                self.player2Score += 1
            if (self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2 and
                self.gameBoard[4][1] == 2 and self.gameBoard[5][0] == 2):
                self.player2Score += 1
            if (self.gameBoard[0][6] == 2 and self.gameBoard[1][5] == 2 and
                self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2):
                self.player2Score += 1
            if (self.gameBoard[1][5] == 2 and self.gameBoard[2][4] == 2 and
                self.gameBoard[3][3] == 2 and self.gameBoard[4][2] == 2):
                self.player2Score += 1
            if (self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2 and
                self.gameBoard[4][2] == 2 and self.gameBoard[5][1] == 2):
                self.player2Score += 1
            if (self.gameBoard[1][6] == 2 and self.gameBoard[2][5] == 2 and
                self.gameBoard[3][4] == 2 and self.gameBoard[4][3] == 2):
                self.player2Score += 1
            if (self.gameBoard[2][5] == 2 and self.gameBoard[3][4] == 2 and
                self.gameBoard[4][3] == 2 and self.gameBoard[5][2] == 2):
                self.player2Score += 1
            if (self.gameBoard[2][6] == 2 and self.gameBoard[3][5] == 2 and
                self.gameBoard[4][4] == 2 and self.gameBoard[5][3] == 2):
                self.player2Score += 1

    def evaluateBoard(self):
        return self.player1Score-self.player2Score
    
    def undoPlayPiece(self,column):
        for i in range(6):
            if self.gameBoard[i][column] != 0:
                self.gameBoard[i][column] = 0
                self.pieceCount -=1
                break 

    def minimax(self,depth,alpha,beta,maxmizingPlayer):
        if depth ==0 or self.pieceCount == 42:
            return self.evaluateBoard()
        
        if maxmizingPlayer: 
            maxEval = float('-inf')
            for col in range(7):
                if self.playPiece(col):
                    eval = self.minimax(depth-1,alpha,beta, False)
                    self.undoPlayPiece(col)
                    minEval = min(beta,eval)
                    alpha=max(alpha,eval)
                    if beta <= alpha: 
                        break 
            return minEval
        else:
            minEval = float('inf')
            for col in range(7):
                if self.playPiece(col):
                    eval = self.minimax(depth-1,alpha,beta,True)
                    minEval = min(minEval,eval)
                    beta = min(beta, eval)
                    if beta <= alpha: 
                        break
            return minEval