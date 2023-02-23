# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 22:22:47 2022

@author: jocelyn
"""

import numpy as np
np.random.rand() #pseudo-random numbers

#using max to avoid going below a certain number
#If you pass max() two arguments, the biggest one gets returned.
#x = max(10, x - 1)

#random number starting from a seed
#same seed same random numbers
#ensures "reproducibility"
np.random.seed(123)
np.random.rand()

#coin toss game.py
coin=np.random.randint(0,2) #randomly generates 0 or 1
print(coin)
if coin==0:
    print("heads")
else:
    print("tails")
    
#to generate random integers, 8 is not included
np.random.randint(4, 8)

#random step 
np.random.seed(123)
outcomes=[]
for x in range(10):
    coin=np.random.randint(0,2)
    if coin == 0:
        outcomes.append("heads")
    else :
        outcomes.append("tails")
print(outcomes)
#random walk, converting this data tracking all steps(random step to random walk)
#also making the process easier
tails=[0]
for x in range(10):
    coin=np.random.randint(0,2)
    tails.append(tails[x]+coin)
print(tails)


#histogram 100 runs
import matplotlib.pyplot as plt
np.random.seed(123)
final_tails=[]
for x in range(1000):
    tails=[0]
    for x in range(10):
        coin=np.random.randint(0,2)
        tails.append(tails[x]+coin)
    final_tails.append(tails[-1])
plt.hist(final_tails,bins=10)
plt.show()    


