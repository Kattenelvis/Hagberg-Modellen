from asyncio.windows_events import NULL
import math
from random import random
import numpy as np
from Household import Household
from Firm import Firm
from Bank import Bank
from State import State
from Common_functions import total
from Initial import * 



class Simulation:

    end_time = end_time

 
    # def __init__(self, ): ***
    firms = [Firm(n) for i in range(n)]
    households = [Household(2, 1) for i in range(n)]


    def time_step(self, t):
        return 1

        
    def simulate(self, end_time):
        for t in range(end_time):
            self.time_step(t)


sim1 = Simulation()
sim1.simulate(20)
print(sim1)