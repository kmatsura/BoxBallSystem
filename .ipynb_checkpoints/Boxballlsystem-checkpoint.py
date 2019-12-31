import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

class Bbs:
    ml = 37#length of box align 
    def __init__(self,array, ml = 37): #"array" represents configuration of balls.
        self.boxlength = ml
        self.box = np.array(array,dtype=int)
        self.carrier = []
        self.energy = 0
        if (len(self.box) < ml): # fill array with empty boxes ubtil its length beccome ml.
            self.box = np.concatenate([self.box,(np.ones(ml - int(len(self.box)),dtype=int))]) 
            
    # Time evolution defined by T = K2K3...Kl+1
    def time_evolve_inf(self, l = 1000):#"l" must be larger than the numbers of ball colors.
        for i in range(l+1,1,-1): #i:l+1 to 2
            count = sum(self.box  == i) # count the number of i-color balls.
            p = 0 
            while count > 0:
                #print(i,count,self.box[p] == i)
                if int(self.box[p]) == i:
                    q = p + 1
                    self.box[p] = 1
                    while q < self.ml+2:
                    
                        if int(self.box[q]) == 1:
                            self.box[q] = -i
                            count -= 1
                            break
                        else:
                            q += 1
                    
                else:
                    p += 1
                    
        self.box = np.abs(self.box)
        
        return self

    # time evolution Tl based on carrier and conbitional R
    def time_evolve(self, l, verbose = True, calc_energy = False):
        self.carrier = [1]*l # declare carrier
        
        if calc_energy == True:
            energy_star = 0
            
        for i in range(len(self.box)):
            self.carrier.sort()
            
            if calc_energy == True:
                if self.box[i] <= self.carrier[0]:
                    energy_star += 1
                
                    
            
            if (self.box[i] > self.carrier[0]):                
                p = len(self.carrier) - 1
                
                while self.carrier[p] >= self.box[i]:
                    p -= 1
                #print(p,self.carrier[p],self.box[i])
                #print("car" + str(self.carrier))
                
                temp = self.box[i]
                self.box[i] = self.carrier[p]
                self.carrier[p] = temp
                
            else:
                temp = self.box[i]
                self.box[i] = self.carrier[l-1]
                self.carrier[l-1] = temp
                
            if verbose == True:
                    print("-" * 50)
                    print("carrier position:" + str(i+1))
                    print("box:" + str(self.box))
                    print("carrier:" + str(self.carrier))
        print("-" * 50)
        
        if calc_energy == True:
            self.energy = len(self.box) - energy_star
            
            
        return self
    
    def reversecarrier_time_evolve(self, l, verbose = True):
        self.carrier = [1]*l # declare carrier
        for i in range(len(self.box)-1,-1,-1):#len(self.box)-1 to 0
            self.carrier.sort()
            if (self.box[i] > self.carrier[0]):
                p = len(self.carrier) - 1
                while self.carrier[p] >= self.box[i]:
                    p -= 1
                #print(p,self.carrier[p],self.box[i])
                #print("car" + str(self.carrier))
                temp = self.box[i]
                self.box[i] = self.carrier[p]
                self.carrier[p] = temp
                
            else:
                temp = self.box[i]
                self.box[i] = self.carrier[l-1]
                self.carrier[l-1] = temp
                
            if verbose == True:
                    print("-" * 50)
                    print("carrier position:" + str(i+1))
                    print("box:" + str(self.box))
                    print("carrier:" + str(self.carrier))
        print("-" * 50)
        return self
        
    def random_bit_inversion(p):
        np.random.choice(p)
        return








def main():
    print('Hello')




if __name__ == '__main__':
    main()
