import numpy as np

class Agent:
    def __init__(self, n):
        self.n=n
        self.nLengthArray = [0 for j in range(0,n)]
        self.amorted, self.debt, self.loan, self.saved = (self.nLengthArray for i in range(4))


    def wage_vector(self, eps, M):
        return np.multiply(np.divide(1, M), eps)


    def calculate_debt(self, interest):
        return np.multiply(np.subtract(np.add(self.debt, self.loan), self.amorted), interest)


    