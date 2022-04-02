import numpy as np

class Agent:
    def __init__(self, n):
        self.n=n
        self.nLengthArray = [0 for j in range(0,n)]
        self.amorted, self.debt, self.loan, self.saved = (self.nLengthArray for i in range(4))


    def wage_vector(self, eps, M):
        return np.multiply(np.divide(1, M), eps)


    def calculate_debt(self, interest):
        return np.multiply(np.subtract(np.add(self.debt, self.loan), self.amorted), interest)


    def calculate_tax(self, floor, necessary, c1, c2, c3, c4, c5, c6, a1, a2):
        #if basic needs aren't met
        if (self.valuesavings < floor):
            if (self.necessary == True):
                self.consumption = necessary
            else:
                #V is PriceVector
                #Tensor product
                self.loan = c1¤V¤necessary
                #from bank
                purchase = necessary
                pay = V¤purchase
                #purchases from Firms
                self.consumption = necessary
                #uses it
        #if basic needs met
        elif (self.valuesavings < roof):
            self.consumption = necessary + c2*(self.savings - necessary)
            purchase = necessary + c3¤normal + c4 ¤leisure
            pay = V¤(purchase)
            if(debt =/= 0vector):
            amorted = a1*debt
            
        
        #if very wealthy
        else:
            self.consumption = self.savings - c5*self.savings
            purchase = necessary + c6*normal + c7*leisure 
            pay = V¤(purchase)
            if(debt =/= 0vector){
            amorted = a2*debt
            
        