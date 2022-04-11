import numpy as np
from Initial import *


class Agent:
    def __init__(self,
                 amort: np.array = zeroArray,
                 debt:  np.array = zeroArray,
                 loan:  np.array = zeroArray,
                 saved: np.array = zeroArray):
        self.amort = amort 
        self.debt = debt 
        self.loan = loan 
        self.saved = saved

    def calculate_debt(self, interest_rate):
        return (self.debt + self.loan - self.amort)*interest_rate


    