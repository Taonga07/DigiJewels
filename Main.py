"""Game of Bejewel made with pygame"""
from random import randint


class GameEngine:
    """Main Game Code"""

    def __init__(self) -> None:
        self.BoardWidth, self.BoardHeight = 5, 5
        self.GameBoard = self.ResetBoard()

    def ResetBoard(self):
        """Restet Board to a random one"""
        Board = []
        for _ in range(self.BoardHeight):
            Board.append([randint(1, 3) for _ in range(self.BoardWidth)])
        return Board

    def Run(self):
        """Main Game Loop"""
        for row in self.GameBoard:
            print(row)
        print(' # ' * self.BoardWidth)
        self.FindTriples()
        for row in self.GameBoard:
            print(row)

    def FindTriples(self):
        """Remove tiles 3 in a row"""
        for i, row in enumerate(self.GameBoard):
            for j, jewel in enumerate(row):
                if 0 < i < (self.BoardWidth - 1):
                    if (jewel == self.GameBoard[i - 1][j]) and (
                        jewel == self.GameBoard[i + 1][j]):
                        self.GameBoard[i][j] = 0
                        self.GameBoard[i - 1][j] = 0
                        self.GameBoard[i + 1][j] = 0
                if 0 < j < (self.BoardHeight - 1):
                    if (jewel == self.GameBoard[i][j - 1]) and (
                        jewel == self.GameBoard[i][j + 1]):
                        self.GameBoard[i][j] = 0
                        self.GameBoard[i][j - 1] = 0
                        self.GameBoard[i][j + 1] = 0


if __name__ == "__main__":
    MyGame = GameEngine()
    MyGame.Run()
