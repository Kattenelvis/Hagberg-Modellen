from pickle import NONE
import numpy as np
from asyncio.windows_events import NULL
from Agent import Agent
from Initial import *


class Household(Agent):      

    def __init__(self, 
                 purchase:          np.array = zeroArray,  
                 consumption:       np.array = zeroArray, 
                 pay:               np.array = zeroArray, 
                 wage:              np.array = zeroArray, 
                 tax:               np.array = zeroArray, 
                 transferal:        np.array = zeroArray, 
                 preferences:       np.array = zeroArray, 
                 purchase_period:   int = 1, 
                 firm_type:         int = None,
                 age:               int = 0):
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

    def utility(self, preferences):
        return np.dot(self.consumption, preferences) 

    #This is always to be calculated before the new consumption
    def output(self):
        return np.dot(inv_input_output, self.consumption)
    def depreciated_goods(self):
        return np.subtract(self.output(), self.consumption)
    
    def getting_wage(self, firm):
        self.wage[1] = firm.pay_wages()/firm.number_of_jobs()
        return self.wage

    def is_employable(self, minAge, maxAge):
        return (minAge < self.age < maxAge)

    def employment_rate(total_consumption, households, standard_work_time):
        employable_number = 0
        employed = (total_consumption[0]*(1/standard_work_time))
        for i in households:
            if i.is_employable() == True:
                employable_number += 1
        employment_rate = employed/employable_number
        return employment_rate

    def change_in_saved(self):
        return (self.depreciated_goods() + self.wage + self.loan - self.amort + self.transferal 
                - self.tax + self.purchase - self.pay)
     
    #This is hypothesis 1, that does not have any buffert
    def consumption_and_purchase(self, necessary, price):
        #Change this if they do not only buy the necessary, differentiate them to include class-differences in spending and consumption
        a1, a2, a3, a4 = np.array([zeroArray for i in range(4)])
        
        normal, leisure = (zeroArray,zeroArray)

        #Lack
        lack = np.subtract(necessary, self.saved)
        lack = lack.clip(min=0) 
        lack_cost = np.dot(lack,price)

        #If basic needs aren't met
        if (lack != zeroArray):
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
        elif (lack == zeroArray):
            self.consumption = necessary + a1*(self.saved - necessary)
            self.purchase = np.add(necessary, np.add(np.multiply(a2, normal), np.multiply(a3, leisure)))
            self.pay[1] = np.dot(price,self.purchase)

            if self.debt != zeroArray:
                self.amort = np.multiply(a4, self.debt)

            
        def will_plan(self, t, interval_type):
            if (t%getattr(self, interval_type) == 0):
                return True
            else:
                return False
