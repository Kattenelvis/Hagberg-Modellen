import numpy as np
from Agent import Agent
from Common_functions import total

class Firm(Agent):             
    savings, debt, consumption, purchase, loan, amorted, tax, transferal, revenue, wage_paid = [np.array([1,4,4,2,3]) for i in range(10)]  
    connections = np.array([0,0,0,0])
    educationsatisfactionperjobtype, jobtypes = (np.array([0,0,0,0]),np.array([0,0,0,0]))

    #Every firm produces one good. "typefirm" describes which good that is, based on it's placement in IO 
    marketshare, firm_type, intelligenceopenness, extraversion = (0,0,0,0)
    psp, pst = (1,1)
   

    def __init__(self, planning_period=1):
        #Number
        prognosis_with_error = self.nLengthArray
        self.planning_period = planning_period
        self.wage_paid = wage_vector[firm_type] * consumption[0]
    

    def plan_consumption(self, pprev):
        
        #pprev is everything that is sold last time period
        #so this is a list of pprev between the beginning of last planning period to now that is summed over
        Average_sold_last_planning_period = sum(pprev) / self.planning_period
        self.consumption = self.Prognosis_with_error * Average_sold_last_planning_period


    #V is price vector
    def plan_prices(self, IO):
        V_new = self.V
        for i in range(len(self.V)):
            for j in range(len(self.V)):
                unit_capital_cost[i] = (IO[j][i] * self.V[j]) 
            
            V_new[i] = self.marketshare[i] * (sum(unit_capital_cost[i]) + wage[i])
        
        return V_new


    def will_plan_consumption(self, t):
        if (t%self.psp == 0):
            return true
        else:
            return false


    def will_plan_prices(self, t):
        if (t%self.pst == 0):
            self.plan_prices()


    def get_worker(self, households):
        for i in range(len(households)):
            if households[i].firm_type == self.firm_type:
                return households[i]


    def saved(self, households, V):
        #modifier for households: (w - pay + purchase)
        #modifier for firms: (- w + revenue - turnover)
        total_household_purchase = total(households, "purchase")
        turnover = np.subtract(self.revenue, total_household_purchase[self.firm_type])
        
        revenue = self.nLengthArray
        revenue[1] = np.dot(turnover, V)

        modifier = np.subtract(np.subtract(revenue, self.wage_paid), turnover)
        
        return np.add(np.subtract(np.add(np.add(np.subtract(self.saved, self.tax), self.transferal), self.loan), self.amorted), modifier) 


    def pay_wages(self, households):
        self.get_worker(households).wage_recieved = self.wage_paid
        self.savings -= self.wage_paid