import numpy as np


class Agent:
    # n=5
    nLengthArray = [0 for j in range(0,5)]
    eps = nLengthArray
    M = nLengthArray

    def wage_vector():
        return np.multiply(np.divide(1,M), eps)