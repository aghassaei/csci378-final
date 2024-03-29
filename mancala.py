import numpy as np

### MANCALA ####

# is updating the state the way i am bad?


class GameEnv:
    def __init__(self):
        self.state = None
        self.count = 0
        self.rng = np.random.randint()
        self.limit = 200 
        # self.state_dim = ????
        self.num_actions = 6

    def reset(self):
        self.state = np.arrray([4,4,4,4,4,4,0,4,4,4,4,4,4,0])
        self.count = 0
        return self.state
    
    def distribute(self, i, pieces, exclude=13):
        while pieces > 0:
            if i == exclude:
                continue
            self.state[i] += 1
            i += 1
            pieces -= 1
        return i
    
    def capture(self, i, store):
        adj = 12 - i
        self.state[store] += self.state[adj]
        self.state[adj] = 0
    
    def rand_agent(self, store=13):
        while True:
            action = self.rng()
            pieces = self.state[action]

            self.state[action] = 0

            self.state, last_idx = self.distribute(self.state, action + 1, pieces, exclude=store)

            if self.state[last_idx] == 1 and last_idx != 13:
                self.state = self.capture(self.state, last_idx, 13)
            if last_idx != 13:
                return
    
    
    def step(self, action):
        self.count += 1

        # Learner's turn. Start by taking pieces out of selected cup
        pieces = self.state[action]
        self.state[action] = 0

        # Distribute pieces
        last_idx = self.distribute(action + 1, pieces, 6)

        # Instead of going again, we skip opponent's turn
        if last_idx == 6:
            return self.end_state()

        # Capture
        if self.state[last_idx] == 1:
            self.state = self.capture(last_idx, 6)

        # Opponent's turn
        
        self.rand_agent()


        return self.end_state()
    
    def end_state(self):
        terminated = self.state[6] > 24 or self.state[13] > 24
        truncated = self.count > self.limit
        if self.state[6] > self.state[13]:
            reward = 1
        else:
            reward = 0
        return self.state, reward, terminated, truncated, {}
    








    @staticmethod
    def format(x):
        if x<10: 
            return "0" + str(x)
        return str(x)
    
    def view(self):
        output = " -----------------------------------\n|  |"
        for i in range(12,6, -1): 
            output.join([" ", format(self.self.state[i]), " |"])
        
        output.join(["|  |\n"])

        for i in range(6): 
            output.join([" ", format(self.self.state[i]), " |"])

        print("Scoreself.state") # TODO
        print(output)
        return None
    
    # def move(self, i):
    #     if self.in_bounds(i) and self.not_empty(i):
    #         pieces = self.self.state[i]
    #         self.self.state[i] = 0
    #         idx = i
    #         while pieces > 0:
    #             if (self.player1 and idx == 13) or (not self.player1 and idx == 6):
    #                 continue
    #             self.self.state[idx] += 1
    #             idx += 1
    #         if (self.player1 and idx == 13) or (not self.player1 and idx == 6):
    #             # go again
    #             pass

    #         if self.self.state[idx] == 1 and self.in_bounds(i): 
    #             self.capture(adj_cup(idx))
    #     self.player = not self.player

    
    # def in_bounds(self, i):
    #     rightside_1 = self.player1 and i in range(6)
    #     rightside_2 = not self.player1 and i in range(7,13)
    #     stores = (i == 6) or (i == 13)
    #     return rightside_1 and rightside_2 and not stores
    
    # def not_empty(self, i):
    #     return (self.player == 0 and self.self.state.side0[i] > 0) or (self.player == 1 and self.self.state.side1[i] > 0)
    
    # def end_game(self):
    #     pass
    
    # def play(self):
    #     g = Game()


