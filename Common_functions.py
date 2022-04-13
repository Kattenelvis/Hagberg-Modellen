import numpy as np
from Initial import n 

def total(sector, which_total):
    sector_size = len(sector)
    # total = np.array([0 for i in range(sector_size)])
    total = np.zeros(n)
    for i in range(sector_size):
        total = np.add(total, getattr(sector[i], which_total))
    return total