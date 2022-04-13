import numpy as np
from Agent import Agent
from Common_functions import total
from Initial import *

class Firm(Agent):   
    
    def __init__(self, 
                 purchase:                  np.array = np.zeros(n),  
                 previous_turnover:         np.array = np.zeros(n),
                 consumption:               np.array = np.zeros(n),
                 wage_markup_relation:      int = 1, 
                 prognosis:                 np.array = np.ones(n),
                 tax:                       np.array = np.zeros(n),
                 transferal:                np.array = np.zeros(n),
                 pay:                       np.array = np.zeros(n),
                 amort:                     np.array = np.zeros(n),
                 debt:                      np.array = np.zeros(n),
                 loan:                      np.array = np.zeros(n),
                 saved:                     np.array = np.zeros(n),
                 firm_number:               int = 2,
                 good_type:                 int = 1,  
                 education_type:            int = 1,
                 price_setting_period:      int = 25,
                 wage_setting_period:       int = 10,
                 production_setting_period: int = 15,
                 purchase_period:           int = 4,  
                 marketshare:               int = 1):
        self.purchase = purchase
        self.previous_turnover = previous_turnover
        self.consumption = consumption
        self.wage_markup_relation = wage_markup_relation
        self.prognosis = prognosis
        self.tax = tax
        self.transferal = transferal
        self.pay = pay
        self.firm_number = firm_number
        self.good_type = good_type
        self.education_type = education_type
        self.price_setting_period = price_setting_period
        self.wage_setting_period = wage_setting_period
        self.production_setting_period = production_setting_period
        self.purchase_period = purchase_period
        self.marketshare = marketshare
        super().__init__(amort, debt, loan, saved)
        
  
    #connections = np.array([0,0,0,0])
    #educationsatisfactionperjobtype, jobtypes = (np.array([0,0,0,0]),np.array([0,0,0,0]))
    #intelligenceopenness, extraversion = (0,0)
    
    #marketshares make up the markup vector
    def marketshare_setting(self, markup):
        self.marketshare = markup[self.firm_number]
        return self.marketshare
    
    #This is always to be calculated before the new consumption
    def output(self):
        return np.dot(inv_input_output, self.consumption)
    
    def produced_and_depreciated_goods(self):
        a = np.subtract(self.output(), self.consumption)
        a[0] = 0
        a[1] = 0
        return(a)
    
    def plan_wages(self):
        wage_payed = (1/(1+self.marketshare)) * self.wage_markup_relation
        return wage_payed 

    def pay_wages(self):
        total_wage_payed = self.plan_wages() * self.consumption[0]
        return total_wage_payed
   
    #The number of jobs at the firm *it is now set to 1 per firm*
    def number_of_jobs(self):
        return 1

    def turnover_and_revenue(self, total_purchase):
        turnover, revenue = [np.zeros(n) for i in range(2)]
        turnover[self.firm_number - 2] = total_purchase
        revenue[1] = np.dot(turnover, price)
        return (turnover, revenue)
    
    def change_in_saved(self, total_purchase):
        wage = np.zeros(n)
        wage[1] = self.pay_wages()
        return (self.produced_and_depreciated_goods() - wage + self.loan - self.amort + self.transferal 
                - self.tax + self.purchase - self.pay - self.turnover_and_revenue(total_purchase)[0] + self.turnover_and_revenue(total_purchase)[1])
    
    def new_saved(self, total_purchase):
        self.saved = self.saved + self.change_in_saved(total_purchase)
        return self.saved
    
    #Is used at the end of each simulated step
    def save_previous_turnover(self, total_purchase):
        self.previous_turnover = self.turnover_and_revenue(total_purchase)[0]
        return self.previous_turnover
        
    
    #Planning consumption
    def plan_consumption(self):
        self.consumption = np.dot(input_output,(self.prognosis * self.previous_turnover))
        return self.consumption

    #This is a total search
    #Is it really -2 here? confusion ***
    def substitution_search_firm(self, firms, input_output):
        for i in range(2,n):
            if (self.consumption[i] >= 1):
                for j in range(2,n):
                    if ((price[i] > price[j]) and firms[i - 2].good_type == firms[j - 2].good_type):
                        self.consumption[j] += self.consumption[i]
                        self.consumption[i] = 0
                        input_output[self.firm_number][j] += input_output[self.firm_number][i]
                        input_output[self.firm_number][i] = 0
        return (self.consumption, input_output)
    
    def purchases(self, debt_floor_firms):
        lack = self.consumption - self.saved
        lack = lack.clip(min=0) 
        lack_cost = np.dot(lack, price)
        if (self.saved[1] >= lack_cost):
            self.purchase = lack
            self.pay[1] = np.dot(self.purchase, price) 
        else:
            if(self.debt[1] < debt_floor_firms):
                if(lack_cost < loan_roof):
                    self.loan[1] = lack_cost
                    self.purchase = lack
                    self.pay[1] = np.dot(self.purchase, price)
                else:
                    self.loan[1] = loan_roof
                    self.consumption = self.saved - lack  
            else: 
                self.consumption = self.saved - lack
                #this is already accounted for in change of savings: self.saved = self.saved - self.consumption

    #Price setting
    def plan_prices(self):
        c1, c2 = (0.05, 0.0)
        production_vector = input_output[self.firm_number]
        unit_cost = np.dot(production_vector, price) + self.plan_wages()
        profit_margin = price[self.firm_number] - unit_cost
        price[self.firm_number] = c1*unit_cost*(1/(1 - self.marketshare)) + c2*profit_margin*(self.marketshare + 1)
        return (unit_cost, profit_margin, price)

    def wage_share(self):
        wage_share = (self.plan_wages() / (self.plan_wages() + self.plan_prices()[1]))
        return wage_share
        

    #Change this constant
    def industrial_growth_percentage(self):
        kaldorian_constant = 1
        kaldorian_growth = (np.dot(self.produced_and_depreciated_goods(), price)/kaldorian_constant)
        return kaldorian_growth


    #I have no idea what this monstrosity is confusion ***
    def answer_application(self, households):
        for i in range(len(households)):
            if (households[i].application(self.firm_number) == self.firm_number):
                workers_number = 0
                for j in range(len(households)):
                    if (households[j].firm_number == self.firm_number):
                        workers_number += 1
                    if ((workers_number/self.consumption[0] > standard_work_time) and (self.saved[0] > standard_work_time*self.plan_wages())):
                        households[i].firm_number = self.firm_number
   