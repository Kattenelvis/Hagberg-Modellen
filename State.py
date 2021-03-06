from Agent import Agent
import numpy as np
from Common_functions import total
from Initial import * 

class State(Agent):
    
    def __init__(self, 
            total_tax:          np.array = np.zeros(n), 
            total_transferal:   np.array = np.zeros(n),
            amort:              np.array = np.zeros(n),
            debt:               np.array = np.zeros(n),
            loan:               np.array = np.zeros(n),
            saved:              np.array = np.zeros(n)):
        self.total_tax = total_tax
        self.total_transferal = total_transferal
        super().__init__(amort, debt, loan, saved)
    
    def saved_state(self):
        return self.saved + self.loan - self.amort + self.total_tax - self.total_transferal
    
