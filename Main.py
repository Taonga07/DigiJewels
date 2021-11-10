from random import randint

class GameEngine:
    def __init__(self) -> None:
        self.BoardWidth, self.BoardHeight = 5, 5
        self.GameBoard = self.ResetBoard()

    def ResetBoard(self):
        Board = []
        for _ in range(self.BoardHeight):
            Board.append([randint(1, 3) for _ in range(self.BoardWidth)])
        return Board

    def Run(self):
        for row in self.GameBoard:
            print(row)


if __name__ == "__main__":
    MyGame = GameEngine()
    MyGame.Run()

