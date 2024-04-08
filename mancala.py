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
        return self.state, reward, terminated, truncated
    








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
    
class DQN(nn.Module):
    
    def __init__(self, state_dim, num_actions):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(state_dim, 20),
            nn.ReLU(),
            nn.Linear(20, 20),
            nn.ReLU(),
            nn.Linear(20, num_actions)
        )

    def forward(self, x):
        return self.model(x)

    def act(self, x):
        return self(x).argmax()
    

class ReplayMemory:

    def __init__(self, cap):
        self.capacity = cap
        self.data = []

    def push(self, state, action, reward, nstate, term):
        if len(self.data) < self.capacity:
            self.data.append((state, action, reward, nstate, term))
        else:
            idx = random.randint(0, self.capacity - 1)
            self.data[idx] = (state, action, reward, nstate, term)

    def sample(self, batch_size):
        return random.sample(self.data, batch_size)

    def __len__(self):
        return len(self.data)