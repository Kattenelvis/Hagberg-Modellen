import numpy as np
from Agent import Agent
from Common_functions import total
from Common_variables import eps, M

class Firm(Agent):             
    savings, debt, consumption, purchase, loan, amorted, tax, transferal, revenue, wage_paid, price_V, pprev = [np.array([1,4,4,2,3]) for i in range(12)]  
    connections = np.array([0,0,0,0])
    educationsatisfactionperjobtype, jobtypes = (np.array([0,0,0,0]),np.array([0,0,0,0]))

    #Every firm produces one good. "typefirm" describes which good that is, based on it's placement in IO 
    marketshare, firm_type, intelligenceopenness, extraversion = (0,0,0,0)
    
    #Interval types
    #time between consumption, prices and wages planning
    psp, pst, wst = (1,1,1)
   

    def __init__(self, n, planning_period=1):
        #Number
        super(Firm, self).__init__(n)
        self.prognosis_with_error = self.nLengthArray
        self.planning_period = planning_period
        self.wage_paid = self.plan_wages()[self.firm_type] * self.consumption[0]
    
    
    def plan_wages(self):
        return np.multiply(np.divide(1, M), eps)

    def plan_consumption(self):
        #pprev is everything that was sold last time period
        #so this is a list of pprev between the beginning of last planning period to now that is summed over
        Average_sold_last_planning_period = sum(self.pprev) / self.planning_period
        return self.prognosis_with_error[self.firm_type] * Average_sold_last_planning_period


    #V is price vector
    def plan_prices(self, input_output):
        V_new = self.price_V
        unit_capital_cost = 0
        for i in range(len(self.price_V)):
            for j in range(len(self.price_V)):
                unit_capital_cost += (input_output[j][i] * self.price_V[j]) 
            
            V_new[i] = self.marketshare * (unit_capital_cost + self.plan_wages()[i])
        
        return V_new


    def will_plan(self, t, interval_type):
        if (t%getattr(self, interval_type) == 0):
            return True
        else:
            return False


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