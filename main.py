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

class Simulation:

    def __init__(self,
                 end_time:      int = 1,
                 firms:         list = zeroArray,
                 households:    list = zeroArray):
        self.end_time = end_time
        
        for i in range(len(firms)): 
            firm = firms[i]       
            firms[i] = Firm(previous_turnover = firm["previous_turnover"], saved = firm["saved"])
        self.firms = firms
        for i in range(len(households)): 
            household = households[i]
            households[i] = Household(firm_type = household["firm_type"], saved = household["saved"], age = household["age"])
        self.households = households


    def employment_rate(self, total_consumption, households, standard_work_time):
        employable_number = 0
        employed = (total_consumption[0]*(1/standard_work_time))
        for i in households:
            if i.is_employable(16, 65) == True:
                employable_number += 1
        employment_rate = employed/employable_number
        return employment_rate

    history = []
    def time_step(self, t):
        
        for i in range(len(self.households)):
            household = self.households[i]
            household.depreciated_goods()
            household.getting_wage(self.firms)
            household.is_employable(16, 65)
            if household.will_plan(t, household.purchase_period):
                household.consumption_and_purchase(necessary, price)
            household.calculate_debt(interest_rate)
            household.change_in_saved()
            household.utility()
            
        for i in range(len(self.firms)):
            firm = self.firms[i]
            firm.marketshare_setting(markup)
            firm.produced_and_depreciated_goods()
            firm.number_of_jobs()
            total_purchase = zeroArray
            total_purchase[firm.firm_type-2]  = total(self.households, "purchase")[firm.firm_type-2] + total(self.firms, "purchase")[firm.firm_type-2] 
            firm.turnover_and_revenue(total_purchase[firm.firm_type-2])
            if firm.will_plan(t, firm.production_setting_period):
                firm.plan_consumption()
            if firm.will_plan(t, firm.purchase_period):
                firm.purchases()
            if firm.will_plan(t, firm.price_setting_period):
                firm.plan_prices()
            firm.wage_share()
            firm.industrial_growth_percentage()
            firm.calculate_debt(interest_rate)
            firm.change_in_saved(total_purchase[firm.firm_type-2])
            firm.save_previous_turnover(total_purchase[firm.firm_type-2])
        
        total_consumption = total(self.households, "consumption") + total(self.firms, "consumption") 
        self.employment_rate(total_consumption, self.households, standard_work_time)
        

        self.history.append(total(self.households, "saved"))

    def simulate(self):
        for t in range(self.end_time):
            self.time_step(t)

simulation = Simulation(end_time, start_firms, start_households)
simulation.simulate()

print(simulation.history)

fig, ax = plt.subplots()
ax.plot([i for i in range(end_time)], simulation.history)
plt.show()