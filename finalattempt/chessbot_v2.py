import chess
import random

def ordered_moves(fen):
    head_board = chess.Board(fen)
    legal_moves = head_board.legal_moves
    moves_dict = dict()
    for move in legal_moves:
        head_board.push(move)
        moves_dict[move] = len(list(head_board.legal_moves))
        head_board.pop()
    sorted_moves = sorted(moves_dict.items(), key=lambda x: x[1])
    return [x[0] for x in sorted_moves]

class ChessBot:
    def __init__(self, board, maxDepth, color):
        self.board = board
        self.maxDepth = maxDepth
        self.color = color
    
    def getBestMove(self):
        return self.engine(None, 1) 

    def evalFunct(self):
        compt = 0
        for i in range(64):
            compt += self.squareResPoints(chess.SQUARES[i])
        compt += self.mateOpportunity() + self.openning() + 0.01 * random.random()
        return compt
    
    def openning(self):
        if self.board.fullmove_number < 10:
            if self.board.turn == self.color:
                return 1 / 30 * len(list(self.board.legal_moves))
            else:
                return -1 / 30 * len(list(self.board.legal_moves))
        else:
            return 0 
    
    def mateOpportunity(self):
        if len(list(self.board.legal_moves)) == 0:
            if self.board.turn == self.color:
                return -9999
            else:
                return 9999
        else:
            return 0
    
    def squareResPoints(self, square):
        pieceValue = 0
        piece = self.board.piece_type_at(square)
        if piece == chess.PAWN:
            pieceValue = 1
        elif piece == chess.ROOK:
            pieceValue = 5.1
        elif piece == chess.BISHOP:
            pieceValue = 3.33
        elif piece == chess.KNIGHT:
            pieceValue = 3.2
        elif piece == chess.QUEEN:
            pieceValue = 8.8
        return pieceValue

    def engine(self, candidate, depth):
        if depth == self.maxDepth or len(list(self.board.legal_moves)) == 0:
            return self.evalFunct()
        else:
            moveList = ordered_moves(self.board.fen())
            newCandidate = None
            if depth % 2 != 0:
                newCandidate = float("-inf")
            else:
                newCandidate = float("inf")

            for move in moveList:
                self.board.push(move)
                value = self.engine(newCandidate, depth + 1)
                self.board.pop()  # Make sure to undo the move after evaluation

                if depth % 2 != 0 and value > newCandidate:
                    newCandidate = value
                    if depth == 1:
                        bestMove = move
                elif depth % 2 == 0 and value < newCandidate:
                    newCandidate = value
                
                if candidate is not None and ((depth % 2 == 0 and value < candidate) or (depth % 2 != 0 and value > candidate)):
                    break

            if depth > 1:
                return newCandidate
            else:
                return bestMove
