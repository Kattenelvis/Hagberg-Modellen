import numpy as np
from Agent import Agent

class Firm(Agent):             
    savings, debt, consumption, purchase, loan, amorted, tax, transferal, revenue = [np.array([1,4,4,2,3]) for i in range(9)]  
    connections = np.array([0,0,0,0])
    educationsatisfactionperjobtype, jobtypes = (np.array([0,0,0,0]),np.array([0,0,0,0]))

    #Every firm produces one good. "typefirm" describes which good that is, based on it's placement in IO 
    marketshare, typefirm, intelligenceopenness, extraversion = (0,0,0,0)
    psp, pst = (1,1)
   

    def __init__(self, planning_period=1):
        #Number
        prognosis_with_error = self.nLengthArray
        self.planning_period = planning_period
    

    def plan_consumption(self):
        
        #pprev is everything that is sold last time period
        #so this is a list of pprev between the beginning of last planning period to now that is summed over
        Average_sold_last_planning_period = sum(pprev) / self.planning_period
        self.consumption = self.Prognosis_with_error * Average_sold_last_planning_period


    def plan_prices(self, IO):
        V_new = self.V
        for i in range(len(self.V)):
            for j in range(len(self.V)):
                V_new[i] = self.marketshare[i] * (IO[j][i] * self.V[j]) 
        
        self.V = V_new


    def will_plan_consumption(self, t):
        if (t%self.psp == 0):
            self.plan_consumption()


    def will_plan_prices(self, t):
        if (t%self.pst == 0):
            self.plan_prices()


    def saved(self, households):
        #modifier for households: (w - pay + purchase)
        #modifier for firms: (- w + revenue - turnover)
        total_household_purchase = total(households, "purchase")
        turnover = np.subtract(self.revenue, total_household_purchase[self.typefirm])
        
        revenue = nLengthArray
        revenue[1] = np.dot(turnover, V)

        modifier = np.subtract(np.subtract(revenue, wage(self)), turnover)
        
        return np.add(np.subtract(np.add(np.add(np.subtract(self.saved, self.tax), self.transferal), self.loan), self.amorted), ) 
