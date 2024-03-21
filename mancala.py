import numpy as np


class Player(i):
    def __init__(self, i):
        self.legal = range(6) if i == 1 else range(6,12)

class Game(player1, player2):
    def __init__(self, player1, player2):
        self.board = np.ones(14) * 4
        self.player1 = player1
        self.player2 = player2
    
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
        # adj side
        # pieces added to your side
        pass

