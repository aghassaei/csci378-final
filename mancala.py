import numpy as np


class Player(i):
    def __init__(self, i):
        self.legal = range(6) if i == 1 else range(6,12)
        self.store = 0


class Board():
    def __init__(self, side1 = np.ones(6) * 4, side2 = np.ones(6) * 4):
        self.side1 = side1
        self.side2 = side2
        self.store1 = 0
        self.store2 = 0
        self.player = True

class Game():
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.log
    
    def move(self, i, player):
        # if legal
        pieces = self.board[i]
        self.board[i]
        while pieces > 0:
            # if wrong mancala, continue
            self.board[i] += 1
            i += 1
        # if self.board[i] == 1: try to capture
        # if self.board[i] is your mancala, go again
    def capture(i):
        # here i is where you landed
        # adj side cleared
        # pieces added to your 
        pass
    
    # def is_legal(self, i):
    #     if (self.board.player and i in range(6) or
    #         not self.board.player and i in range():
    #         True
