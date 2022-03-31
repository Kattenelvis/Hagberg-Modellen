from Agent import Agent
import numpy as np
from Common_functions import total

class State(Agent):
    def total_saved(self, firms, households):
        return np.subtract(np.subtract(np.add(np.add(self.saved, total(firms, "tax")), total(households, "tax")), total(households, "transferal")), total(firms, "transferal"))  
