import numpy as np
from Initial import *


class Agent:
    def __init__(self,
                 amort: np.array = np.zeros(n),
                 debt:  np.array = np.zeros(n),
                 loan:  np.array = np.zeros(n),
                 saved: np.array = np.zeros(n)):
        self.amort = amort 
        self.debt = debt 
        self.loan = loan 
        self.saved = saved

    def calculate_debt(self, interest_rate):
        return (self.debt + self.loan - self.amort)*interest_rate

    def will_plan(self, t, interval_type):
        return (t%interval_type == 0 and t != 0)

    