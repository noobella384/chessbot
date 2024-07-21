import chess
import chessbot


class final_engine:
    def __init__(self, board=chess.Board):
        self.board=board

    def HumanMove(self):
        try:
            print([move for move in self.board.legal_moves])
            print("Or")
            print([move.uci() for move in self.board.legal_moves])
            print("""To undo your last move, type "undo".""")

            play = input("Your move: ")
            if (play=="undo"):
                self.board.pop()
                self.board.pop()
                self.HumanMove()
                return
            self.board.push_san(play)
        except:
            try:
                self.board.push_uci(play)
            except:
                self.HumanMove()

    def EngineMove(self, maxDepth, color):
        engine = chessbot.chessbot(self.board, maxDepth, color)
        self.board.push(engine.getBestMove())

    def startGame(self):
        color=None
        while(color!="b" and color!="w"):
            color = input("""Play as (type "b" or "w"): """)
        maxDepth=None
        while(isinstance(maxDepth, int)==False):
            maxDepth = int(input("""Choose Depth: """))
        if color=="b":
            while(self.board.is_checkmate()==False):
                print("The engine is thinking...")
                self.EngineMove(maxDepth, chess.WHITE)
                print(self.board)
                self.HumanMove()
                print(self.board)
            print(self.board)
            print(self.board.outcome())

        elif color=="w":
            while (self.board.is_checkmate()==False):
                print(self.board)
                self.HumanMove()
                print(self.board)
                print("The engine is thinking...")
                self.EngineMove(maxDepth, chess.BLACK)
            print(self.board)
            print(self.board.outcome())

        self.board.reset
        self.startGame()

newBoard=chess.Board()
game= final_engine(newBoard)
start=game.startGame()