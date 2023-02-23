# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 22:29:37 2022

@author: jocelyn
"""

#Empire state building game - hacker statistics
#You made a bet with a friend based on a game where you state you will be able to reach step 60 of the empire state
#You will throw a dice 100 times
#If you get "1" or "2", you need to go 1 step down (-1)
# throwing "3","4" or "5" makes you go 1 step up(+1)
#If you throw 6, that allows you to throw dice 1 more time and the number you get is the number of steps you will go up
#It is not possible to go below step 0
#As you are a bit clumsy, there is 0.1% chance of you falling down the stairs, that means, starting all over again
#We will make a code to see based on statistics what is your chance of winning this bet

import numpy as np
import matplotlib.pyplot as plt

print(np.random.randint(1,7))


#initialize all_walks (so we can make distribution)
all_walks=[]
#simulate random walk x times
for i in range (500):

# Initialize random_walk
    random_walk =[0]

    for x in range(100) :
    # Set step: last element in random_walk
        step=random_walk[-1]
    # Roll the dice
        dice = np.random.randint(1,7)

    # Determine next step
        if dice <= 2:
            step=max(0,step-1) #this will help us avoid going below 0
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
            # Implement clumsiness
        if np.random.rand()<= 0.001:
            step = 0
    # append next_step to random_walk
        random_walk.append(step)
    all_walks.append(random_walk)
# Print random_walk
print(random_walk)
print(all_walks)
# Plot random_walk
plt.plot(random_walk)
# Show the plot
plt.show()

#making a distribution after trying this 100 times

# Convert all_walks to NumPy array: np_aw
np_aw=np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
#plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t=np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()

#getting the probability of you getting to step 60
# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

#final step, actually getting the probability of winning!
print(np.mean(ends>=60))