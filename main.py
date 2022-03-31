from asyncio.windows_events import NULL
import math
from random import random
import numpy as np
# import setUpVariables
from Household import Household
from Firm import Firm

n=5
nLengthArray = [0 for j in range(0,n)]



def total(sector, which_total):
    sector_size = len(sector)
    total = np.array([0 for i in range(sector_size)])
    for i in range(sector_size):
        print(sector[i].consumption)
        total = np.add(total, getattr(sector[i], which_total))
    #sum sector.consupmtion
    return total




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

DebtBank, DebtState, LoansState, bank_loaned, bank_amorted, AmortedState = [nLengthArray for i in range(6)]
state_saved, bank_saved = (nLengthArray, nLengthArray)


def saved_state(firms, households):
    return np.subtract(np.subtract(np.add(np.add(state_saved, total(firms, "tax")), total(households, "tax")), total(households, "transferal")), total(firms, "transferal"))  


def saved_bank():
    return np.add(np.subtract(bank_saved, bank_loaned), bank_amorted) #+ (CreatedTokens - DestroyedTokens)


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



def employable(minAge, maxAge, households):
    #for every household: if age > minAge and < maxAge, add +1 to some number all divided by N
    return 0

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

    firm_list = [Firm for i in range(n)]
    household_list = [Household for i in range(n)]
    # IO = np.array([[0 for j in range(0,n)] for i in range(0,n)])
    IO = np.array([
        [0,2,0,1,2],
        [0,0,4,0,1],
        [0,3,0,5,1],
        [2,1,6,0,0],
        [1,2,7,9,0]
    ])
    # def __init__(self, ):
    firms = [Firm for i in range(n)]
    households = [Household for i in range(n)]
        

    def time_step(self):

        output = np.dot(np.linalg.inv(self.IO), np.add(total(self.firms, "consumption"), total(self.households, "consumption")))
        
        #Labour hours
        L = self.IO[0]

        #productivity
        m = output/L

        consumed_labour_hours = total(self.firm_list, "consumption")[0]

        # Total worked hours
        e = (consumed_labour_hours / standard_work_time) / (self.N*employable(16,65, self.household_list))

        # Wages
        total_wages = total(self.household_list, "wages")

        wage_share = total_wages/output
        
        #Taxes will come in if statements
   
        

        #Kaldorian equation for industrial growth 
        å =  np.multiply(np.dot(output, V), kald)

        #Death Probability


    def simulate(self, T):
        for i in range(T):
            self.time_step()



# sim1 = Simulation()
# sim1.time_step([2,2,2,2,2])

#household.valuesavings is the dot product of the price vector with houshold savings

        #if poor
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

# import random
# testsimulation = Simulation(4,661,2)
# testsimulation1 = Simulation(random.Random.random(),66,1)

# testsimulation.time_step()

# Netflix = Firm
# print(calculate_debt(Netflix, np.array([1,1,1,1,1])))
# # print(np.multiply(np.array([2,2]), np.array([2,2])))

sim1 = Simulation()
sim1.simulate(20)