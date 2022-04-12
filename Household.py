from pickle import NONE
import numpy as np
from asyncio.windows_events import NULL
from Agent import Agent
from Initial import *


class Household(Agent):      

    def __init__(self, 
                 purchase:          np.array = np.zeros(n),  
                 consumption:       np.array = np.zeros(n), 
                 pay:               np.array = np.zeros(n), 
                 wage:              np.array = np.zeros(n), 
                 tax:               np.array = np.zeros(n), 
                 transferal:        np.array = np.zeros(n), 
                 preferences:       np.array = oneArray, 
                 amort:             np.array = np.zeros(n),
                 debt:              np.array = np.zeros(n),
                 loan:              np.array = np.zeros(n),
                 saved:             np.array = np.zeros(n),
                 purchase_period:   int = 1, 
                 firm_type:         int = 2,
                 age:               int = 16):
        self.purchase = purchase
        self.consumption = consumption 
        self.pay = pay 
        self.wage = wage
        self.tax = tax
        self.transferal = transferal 
        self.preferences = preferences
        self.purchase_period = purchase_period
        self.firm_type = firm_type
        self.age = age
        super().__init__(amort, debt, loan, saved)

    def utility(self):
        return np.dot(self.consumption, self.preferences) 

    #This is always to be calculated before the new consumption
    def output(self):
        return np.dot(inv_input_output, self.consumption)
    def depreciated_goods(self):
        return np.subtract(self.output(), self.consumption)
    
    def getting_wage(self, firms):
        self.wage[1] = firms[self.firm_type-2].pay_wages()/firms[self.firm_type-2].number_of_jobs()
        return self.wage

    def is_employable(self, minAge, maxAge):
        return (minAge < self.age < maxAge)

    def change_in_saved(self):
        return (self.depreciated_goods() + self.wage + self.loan - self.amort + self.transferal 
                - self.tax + self.purchase - self.pay)
     
    def new_saved(self):
        self.saved += self.change_in_saved()
        return self.saved
    
    #This is hypothesis 1, that does not have any buffert
    def consumption_and_purchase(self, necessary, price):
        #Change this if they do not only buy the necessary, differentiate them to include class-differences in spending and consumption
        a1, a2, a3, a4 = np.array([zeroArray for i in range(4)])
        
        normal, leisure = (zeroArray,zeroArray)

        #Lack of goods to survive
        lack = np.subtract(necessary, self.saved)
        lack = lack.clip(min=0) 
        lack_cost = np.dot(lack,price)
        

        #If basic needs aren't met
        if (any(lack != zeroArray)):
            #If the household affords the lack
            if (self.saved[1] >= lack_cost):
                self.purchase = lack
                self.pay[1] = lack_cost
                self.consumption = necessary
            else:
                #If the household does not afford the lack they loan that amount
                self.loan[1] = lack_cost
                self.purchase = lack
                self.pay[1] = lack_cost
                self.consumption = necessary

        #If basic needs are met
        elif (any(lack == zeroArray)):
            self.consumption = necessary + a1*(self.saved - necessary)
            self.purchase = np.add(necessary, np.add(np.multiply(a2, normal), np.multiply(a3, leisure)))
            self.pay[1] = np.dot(price,self.purchase)

            if any(self.debt != zeroArray):
                self.amort = np.multiply(a4, self.debt)

            

            