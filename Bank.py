from Agent import Agent
import numpy as np
from Initial import * 

class Bank(Agent):

    def __init__(self, 
                tokens_created:     np.array = zeroArray, 
                tokens_destroyed:   np.array = zeroArray,
                amort:              np.array = zeroArray,
                debt:               np.array = zeroArray,
                loan:               np.array = zeroArray,
                saved:              np.array = zeroArray):
            self.tokens_created = tokens_created
            self.tokens_destroyed = tokens_destroyed
            super().__init__(amort, debt, loan, saved)
    
    def saved_bank(self):
        return self.saved - self.loan + self.amort + self.tokens_created - self.tokens_destroyed
    
    #Hypothesis 1, banks only create tokens when under some floor in savings
    def credit_expansion(self, floor):
        if (self.saved[1] < floor):
            self.tokens_created = floor

