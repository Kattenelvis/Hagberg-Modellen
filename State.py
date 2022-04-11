from Agent import Agent
import numpy as np
from Common_functions import total
from Initial import * 

class State(Agent):
    
    def __init__(self, 
            total_tax:          np.array = zeroArray, 
            total_transferal:   np.array = zeroArray):
        self.total_tax = total_tax
        self.total_transferal = total_transferal
    
    def saved_state(self):
        return self.saved + self.loan - self.amort + self.total_tax - self.total_transferal
    
