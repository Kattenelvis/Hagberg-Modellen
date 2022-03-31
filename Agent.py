import numpy as np

class Agent:
    # n=5
    nLengthArray = [0 for j in range(0,5)]
    
    #TODO: Get rid of these in the Agent class and make them inputs in functions they're needed in
    eps = nLengthArray
    M = nLengthArray

    def __init__(self):
        self.amorted, self.debt, self.loan, self.saved = (self.nLengthArray for i in range(4))

    def wage_vector(self):
        return np.multiply(np.divide(1,self.M), self.eps)