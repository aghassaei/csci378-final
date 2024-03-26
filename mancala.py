import numpy as np

### MANCALA ####


# Returns cup index on opposite side of the board
def adj_cup(n):
    return 12 - n


class Game:
    def __init__(self):
        self.board = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
        self.log = []
        self.player1 = True
        self.state = None
        self.count = 0
        self.rng = np.random.default_rng()
        self.limit = 200 

    @staticmethod
    def format(x):
        if x<10: 
            return "0" + str(x)
        return str(x)
    
    def view(self):
        output = " -----------------------------------\n|  |"
        for i in range(12,6, -1): 
            output.join([" ", format(self.board[i]), " |"])
        
        output.join(["|  |\n"])

        for i in range(6): 
            output.join([" ", format(self.board[i]), " |"])

        print("Scoreboard") # TODO
        print(output)
        return None
    
    def move(self, i):
        if self.in_bounds(i) and self.not_empty(i):
            pieces = self.board[i]
            self.board[i] = 0
            idx = i
            while pieces > 0:
                if (self.player1 and idx == 13) or (not self.player1 and idx == 6):
                    continue
                self.board[idx] += 1
                idx += 1
            if (self.player1 and idx == 13) or (not self.player1 and idx == 6):
                # go again
                pass

            if self.board[idx] == 1 and self.in_bounds(i): 
                self.capture(adj_cup(idx))
        self.player = not self.player
    def capture(i):
        pieces = self.board[i]
        self.board[i] = 0
        if self.player1:
            self.board[6] += pieces
        else:
            self.board[13] += pieces
        return 
    
    def in_bounds(self, i):
        rightside_1 = self.player1 and i in range(6)
        rightside_2 = not self.player1 and i in range(7,13)
        stores = (i == 6) or (i == 13)
        return rightside_1 and rightside_2 and not stores
    
    def not_empty(self, i):
        return (self.player == 0 and self.board.side0[i] > 0) or (self.player == 1 and self.board.side1[i] > 0)
    
    def end_game(self):
        pass
    
    def play(self):
        g = Game()


    def reset(self, random=True):
        if random:
            # reset randomly
            pass



    def step(self):
        pass
