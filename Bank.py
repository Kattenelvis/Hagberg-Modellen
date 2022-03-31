from Agent import Agent
import numpy as np

class Bank(Agent):
    def saved_bank(self):
        return np.add(np.subtract(self.saved, self.loan), self.amorted)