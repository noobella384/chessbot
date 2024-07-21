import chess
import random
from chessbot_v2 import ordered_moves
class chessbot:
    def __init__(self, board, maxDepth, color):
        self.board=board
        self.maxDepth=maxDepth
        self.color=color
    
    def getBestMove(self):
        return self.engine(None, 1) 

    def evalFunct(self):
        compt =0
        for i in range(64):
            compt= compt + int(self.squareResPoints(chess.SQUARES[i]))
        compt= compt + int(self.mateOpportunity())+0.01*random.random()
        return compt
    
    def mateOpportunity(self):
        if (self.board.legal_moves.count()==0):
            if (self.board.turn == self.color):
                return -9999
            else:
                return 9999
        else:
            return 0
    
    def squareResPoints(self, square):
        pieceValue=0
        if(self.board.piece_type_at(square) == chess.PAWN):
            pieceValue=1
        elif(self.board.piece_type_at(square) == chess.ROOK):
            pieceValue=5.1
        elif(self.board.piece_type_at(square) == chess.BISHOP):
            pieceValue=3.2
        elif(self.board.piece_type_at(square) == chess.KNIGHT):
            pieceValue=3
        elif(self.board.piece_type_at(square) == chess.QUEEN):
            pieceValue=8.9
        
        if (self.board.color_at(square)!=self.color):
            return -pieceValue
        else:
            return pieceValue
        

    def engine(self, candidate, depth):
        if(depth == self.maxDepth or self.board.legal_moves.count()==0):
            return self.evalFunct()
        else:
            moveList = ordered_moves(self.board.fen())
            print(moveList)

            newCandidate=None

            if(depth%2 !=0):
                newCandidate=float("-inf")
            else:
                newCandidate=float("inf")

            for i in moveList:
                print(i)
                self.board.push(i)
                value = self.engine(newCandidate, depth+1)

                if(value > newCandidate and depth % 2 !=0):
                    newCandidate=value
                    if(depth==1):
                        move=i
                    

                elif(value < newCandidate and depth%2==0):
                    newCandidate=value
                
                if(candidate !=None and value < candidate and depth %2 ==0):
                    self.board.pop()
                    break

                elif(candidate != None and value> candidate and depth%2 !=0):
                    self.board.pop()
                    break
                
                self.board.pop()
        if(depth>1):
            return newCandidate
        else:
            return move
        


                


