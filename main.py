from asyncio.windows_events import NULL
import math
from random import random
import numpy as np
# import setUpVariables
from Household import Household
from Firm import Firm
from Bank import Bank
from State import State
from Common_functions import total

n=5
nLengthArray = [0 for j in range(0,n)]

# consumptionFirm = Total(All_firms, "consumption")
    


    #  TaxFirm = ;//Summing
    #  TaxHousehold = ;//Summing
    #  TransferalHousehold = ;//Summing
    #  TransferalFirm = ;//Summing
    #  LoansHousehold = ;//Summing
    #  LoansFirm = ;//Summing
    #  AmortedHousehold = ;//Summing
    #  AmortedFirm = ;//Summing
    #  DebtHousehold = ;//Summing
    #  DebtFirm = ;//Summing
    
    #  ?:
    #  TaxBank 
    #  TransferalBank 

state_saved, bank_saved = (nLengthArray, nLengthArray)




 #+ (CreatedTokens - DestroyedTokens)


#Interest rates ?
i = nLengthArray

standard_work_time = 8 

#TODO: Comment what each of these variables are
m, O, L, w, eps, ws, pst = [nLengthArray for i in range(7)]
e = 0    
 
#Powershare 
ps = nLengthArray
#preference vector
u = nLengthArray
#Utility
U = 0

#Industrial growth prognosis
å = nLengthArray
#The kaldorian proportionality constant; can vary, not between time steps though, if it does Kaldor is wrong
kald = 0.5; 

#Change in token amount
CreatedTokens = nLengthArray
DestroyedTokens = nLengthArray

#Markup is the vector of all marketshares 
M = nLengthArray

#Beta, the planning error ?
# beta = nLengthArray

#Purchases
p = nLengthArray

#Pprev set some start state; does not change except for start state
pprev = [nLengthArray]


# Input Output Model, all resources and types of labour in society.
#First row is for labour hours, second row and below is for tokens and below that comes goods. 

IO = np.array([[0 for j in range(0,n)] for i in range(0,n)])

# class Agent:
def calculate_debt(agent, interest):
    return np.multiply(np.subtract(np.add(agent.debt, agent.loan), agent.amorted), interest)

def saved(agent, modifier):
    #modifier for households: (w - pay + purchase)
    #modifier for firms: (- w + sales - turnover)
    return np.add(np.subtract(np.add(np.add(np.subtract(agent.saved, agent.tax), agent.transferal), agent.loan), agent.amorted), modifier) 

#the n:th position in this vector represents the wage paid out in tokens for firm type n
def wage_vector():
    return np.multiply(np.divide(1,M), eps)




V = nLengthArray




# Environments = [Firm, Firm, Firm]


#class State
#class Bank        


class Simulation:
    #Population, always equal to number of households
    N = 0
    #Time
    t = 0
    #End Time
    T = 10
    #Number of goods and tokens in the economy, plus one for workhours
    n = 5

    # IO = np.array([[0 for j in range(0,n)] for i in range(0,n)])
    IO = np.array([
        [0,2,0,1,2],
        [0,0,4,0,1],
        [0,3,0,5,1],
        [2,1,6,0,0],
        [1,2,7,9,0]
    ])
    # def __init__(self, ):
    firms = [Firm() for i in range(n)]
    households = [Household(2, 1) for i in range(n)]

    def employable(self, minAge, maxAge):
        total_employable = 0
        for i in range(len(self.households)):
            if self.households[i].is_employable(minAge, maxAge):
                total_employable+=1
        
        return total_employable

    def time_step(self):
    
        output = np.dot(np.linalg.inv(self.IO), np.add(total(self.firms, "consumption"), total(self.households, "consumption")))

        print(output)    
        #Labour hours
        L = self.IO[0]

        #productivity
        m = output/L

        consumed_labour_hours = total(self.firms, "consumption")[0]

        # Total worked hours
        e = (consumed_labour_hours / standard_work_time) / (self.N*self.employable(16,65))

        # Wages
        total_wages = total(self.households, "wage")

        wage_share = total_wages/output
        
        #Taxes will come in if statements
   
        

        #Kaldorian equation for industrial growth 
        å =  np.multiply(np.dot(output, V), kald)

        #Death Probability


    def simulate(self, T):
        for i in range(T):
            self.time_step()



#household.valuesavings is the dot product of the price vector with houshold savings

        #if very poor
        # if (household.valuesavings < floor) {
        #     if (household.necessary === true){
        #         household.consumption = necessary
        #     }
        #     else {
        #     #V is PriceVector
        #     #Tensor product
        #     household.loan = c1¤V¤necessary
        #     #from bank
        #     purchase = necessary
        #     pay = V¤purchase
        #     #purchases from Firm
        #     household.consumption = necessary
        #     #uses it
        #     }
        # }
        # #if basic needs met
        # elseif (household.valuesavings < roof){
        #     household.consumption = necessary + c2*(household.savings - necessary)
        #     purchase = necessary + c3¤normal + c4¤leisure
        #     pay = V¤(purchase)
        #     if(debt =/= 0vector){
        #       amorted = a1*debt
        #     }
        # }
        # #if bourgouise
        # else {
        #     household.consumption = household.savings - c5*household.savings
        #     purchase = necessary + c6*normal + c7*leisure 
        #     pay = V¤(purchase)
        #     if(debt =/= 0vector){
        #       amorted = a2*debt
        #     }
        # }


# If (age === employable or something like that) {
#         #Probability distribution where most probable if childless, straight (sexuality === 0), and are similar by weights where opposite in agreeableness and neuroticism is the 
#         #case and parents can not be the same. This is checked over the network (connections), over some amount of timesteps.
#     };


sim1 = Simulation()
sim1.simulate(20)