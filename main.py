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
import matplotlib.pyplot as plt
from copy import deepcopy

class Simulation:

    def __init__(self,
                 end_time:      int = 1,
                 firms:         list = np.zeros(n),
                 households:    list = np.zeros(n),
                 bank:          Bank = Bank()):
        self.end_time = end_time
        self.bank = bank
        
        for i in range(len(firms)): 
            firm = firms[i]       
            firms[i] = Firm(previous_turnover = firm["previous_turnover"], saved = firm["saved"], prognosis = np.array(firm["prognosis"]), firm_number = firm["firm_number"], price_setting_period = firm["price_setting_period"])
        self.firms = firms
        for i in range(len(households)): 
            household = households[i]
            households[i] = Household(firm_number = household["firm_number"], saved = household["saved"], age = household["age"])
        self.households = households


    def employment_rate(self, total_consumption, households, standard_work_time):
        employable_number = 0
        employed = (total_consumption[0]*(1/standard_work_time))
        for i in households:
            if i.is_employable(16, 65) == True:
                employable_number += 1
        employment_rate = employed/employable_number
        return employment_rate


    history = {"total_firm_consumption": [], "total_household_consumption": [], "household_0_savings": [],
               "total_household_debt": [], "price": [], "total_savings": [], "token_amount": [], "total_loans": []}
    def time_step(self, t):
        for i in range(len(self.households)):
            household = self.households[i]
            household.depreciated_goods()
            household.getting_wage(self.firms)
            household.is_employable(16, 65)
            if household.will_plan(t, household.search_period):
                household.substitution_search_household(necessary, price, self.firms)
            if household.will_plan(t, household.purchase_period):
                household.consumption_and_purchase(necessary, price, debt_floor_households)
            household.calculate_debt(interest_rate)
            household.change_in_saved()
            household.new_saved()
            household.utility()
            if household.will_plan(t, household.job_search_period):
                household.labor_market_search(self.firms)
            
        for i in range(len(self.firms)):
            firm = self.firms[i]
            firm.marketshare_setting(markup)
            firm.number_of_jobs()
            total_purchase = np.zeros(n)
            total_purchase[firm.firm_number]  = total(self.households, "purchase")[firm.firm_number] + total(self.firms, "purchase")[firm.firm_number] 
            firm.turnover_and_revenue(total_purchase[firm.firm_number])
            if firm.will_plan(t, firm.production_setting_period):
                firm.plan_consumption()
            if firm.will_plan(t, firm.purchase_period):
                firm.purchases(debt_floor_firms)
            if firm.will_plan(t, firm.price_setting_period):
                firm.plan_prices()
            firm.wage_share()
            firm.industrial_growth_percentage()
            firm.calculate_debt(interest_rate)
            firm.change_in_saved(total_purchase[firm.firm_number])
            firm.new_saved(total_purchase[firm.firm_number])
            firm.save_previous_turnover(total_purchase[firm.firm_number])
            firm.answer_application(self.households)
            
        self.bank.credit_expansion(100)
        self.bank.saved_bank()
            
            
        total_consumption = total(self.households, "consumption") + total(self.firms, "consumption") 
        self.employment_rate(total_consumption, self.households, standard_work_time)


        self.history["total_firm_consumption"].append(total(self.firms, "consumption"))
        self.history["total_household_consumption"].append(total(self.households, "consumption"))
        self.history["household_0_savings"].append(self.households[0].saved)
        self.history["total_household_debt"].append(self.households[0].debt)
        self.history["total_savings"].append(total(self.firms, "saved")+total(self.households, "saved")+self.bank.saved)
        self.history["token_amount"].append(self.firms[0].saved[1]+self.households[0].saved[1]+self.bank.saved[1])
        self.history["total_loans"].append(self.firms[0].loan[1]+self.households[0].loan[1])



    def simulate(self):
        for t in range(self.end_time):
            self.time_step(t)

simulation = Simulation(end_time, start_firms, start_households)
simulation.simulate()


fig, ax = plt.subplots()
ax.plot([i for i in range(end_time)], simulation.history["total_firm_consumption"])
plt.show()

#TODO fix the problem of firms having no consumption yet having production, and to standardize 
# the firm_number - 2 problem, as well as test multiple inputs