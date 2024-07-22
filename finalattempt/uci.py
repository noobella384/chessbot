import chess
import chessbot
import sys

class UCIEngine:
    def __init__(self):
        self.board = chess.Board()
        self.maxDepth = None

    def set_option(self, name, value):
        # Handle options here if needed
        pass

    def position(self, command):
        parts = command.split()
        index = parts.index("moves") if "moves" in parts else len(parts)
        if "fen" in parts:
            fen = " ".join(parts[1:index])
            self.board.set_fen(fen)
        else:
            self.board.reset()
        for move in parts[index + 1:]:
            self.board.push_uci(move)

    def go(self, command):
        parts = command.split()
        for i in range(len(parts)):
            if parts[i] == "depth":
                self.maxDepth = int(parts[i + 1])
        engine = chessbot.chessbot(self.board, self.maxDepth, self.board.turn)
        best_move = engine.getBestMove()
        self.board.push(best_move)
        print(f"bestmove {best_move.uci()}")

    def uci_loop(self):
        while True:
            try:
                command = input()
                if command == "uci":
                    self.uci()
                elif command == "isready":
                    print("readyok")
                elif command.startswith("setoption"):
                    parts = command.split("name ", 1)[1].split(" value ")
                    name = parts[0]
                    value = parts[1] if len(parts) > 1 else None
                    self.set_option(name, value)
                elif command == "ucinewgame":
                    self.board.reset()
                elif command.startswith("position"):
                    self.position(command)
                elif command.startswith("go"):
                    self.go(command)
                elif command == "quit":
                    break
            except Exception as e:
                print(f"info string Error: {e}")

    def uci(self):
        print("id name MyUCIEngine")
        print("id author YourName")
        # Add any options you want to support here
        print("uciok")

if __name__ == "__main__":
    engine = UCIEngine()
    engine.uci_loop()
