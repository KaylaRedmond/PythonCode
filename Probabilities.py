import math
import numpy as np
import scipy
from scipy import stats
from scipy.stats import binom
from scipy.stats import poisson
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.optimize import curve_fit
from scipy.stats import norm
from random import randint
from collections import Counter


a=[]
num_games = 2000


for n in range(num_games):
    num_flips = 0
    win = 0
    while win == 0:
        turn = np.random.randint(0,2) + np.random.randint(0,2) + np.random.randint(0,2) + np.random.randint(0,2) + np.random.randint(0,2)
        num_flips += 1
        if turn == 1:
            win += 1
            a.append(num_flips/2)
    
# print a

print("Mean number of flips", np.mean(a))
# print Counter(a)

labels, values = zip(*Counter(a).items())
indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(np.arange(1.0,max(indexes),2.0))
plt.xlabel('Number of Flips')
plt.ylabel('Number of Occurrences')
plt.show()


# introduce bias into one coin
# B is probability of heads
# I set 0 to be heads, 1 to be tails

B = .3

for n in range(num_games):
    num_flips = 0
    win = 0
    while win == 0:
        turn = np.random.choice([0,1],p=[B,1-B]) + np.random.randint(0,2) + np.random.randint(0,2) + np.random.randint(0,2) + np.random.randint(0,2)
        num_flips += 1
        if turn == 1:
            win += 1
            a.append(num_flips)
    
# print a

print( "Mean number of flips", np.mean(a))
# print Counter(a)

labels, values = zip(*Counter(a).items())
indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(np.arange(1.0,max(indexes),3.0))
plt.xlabel('Number of Flips')
plt.ylabel('Number of Occurrences')
plt.show()







    
            
            
        

