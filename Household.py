import numpy as np
from asyncio.windows_events import NULL
from Agent import Agent

class Household(Agent):      

    def __init__(self, numChildren, n):
        self.children = np.array([0 for j in range(0, numChildren)])
        self.savings, self.tax, self.transferal, self.purchase, self.consumption, self.pay, self.wage = np.array([self.nLengthArray for i in range(0,7)])

    sex, sexuality, language, ethnicity, disability, culturaladherence, attractiveness, firm_type, age = (0,0,0,0,0,0,0,NULL,0)
    intelligenceopenness, conscientiousness, secularrational, selfexpressivity, agreeableness, extraversion, neuroticism = (0,0,0,0,0,0,0)
    
    parents = np.array([0,0])
    education = np.array([0,0,0,0])
    connections = np.array([0,0,0,0])


    # Each worker is employed at a firm, which has a certain marketshare which determines the wage.
    #l is worked hours


    # def deathProbability():

    #Utility per household with some preferences
    def utility(self, preferences, ps):
        return np.dot(np.multiply(ps, self.consumption), preferences) 


    def total_saved(self, firms, households, n, V):
        total_household_purchase = self.total(households, "purchase")
        turnover = np.subtract(self.revenue, total_household_purchase[self.typefirm])
        
        pay_mod = [1 for i in range(n)]
        pay_mod[1] = np.dot(self.pay, V)

        wage = self.nLengthArray
        wage[1] = self.wage_vector()[self.firm_type] * firms[self.firm_type].consumption[0]
        
        #modifier for households: (wage - pay_mod + purchase)
        #modifier for firms: (- wage + revenue - turnover)
        modifier = np.subtract(np.subtract(pay_mod, turnover), wage)

        return np.add(np.subtract(np.add(np.add(np.subtract(self.saved, self.tax), self.transferal), self.loan), self.amorted), modifier) 


    def is_employable(minAge, maxAge, households):
    #for every household: if age > minAge and < maxAge, add +1 to some number all divided by N
        return True