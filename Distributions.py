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


# After installing python, in the python folder, under Scripts, are the pip files
# To install numpy, enter the command prompt on Windows within the Scripts
# folder, type pip install numpy
# Then you can import numpy in the Python scripts





# Binomial Distribution

# first trial with p=.35, N=4
N = 4
p = .35
# going out to 8 successes
# produce evenly spaced values starting from 0 out to 8
k = np.arange(0,8)
# probability mass function for binomial distribution
binomial_trial_i = stats.binom.pmf(k, N, p)
# print binomial_trial_i

#plt.plot(k, binomial_trial_i, 'o-')
#plt.title ('Binomial: N = 4, p = .35')
#plt.xlabel('Number of successes')
#plt.ylabel('Probability of successes')
#plt.show()



# second trial with p=.35, N=40
N = 40
p = .35
# going out to 30 successes
k = np.arange(0,30)
binomial_trial_ii = stats.binom.pmf(k, N, p)
# print binomial_trial_ii

#plt.plot(k, binomial_trial_ii, 'o-')
#plt.title ('Binomial: N = 40, p = .35')
#plt.xlabel('Number of successes')
#plt.ylabel('Probability of successes')
#plt.show()





# Poisson Distribution

# first trial with p=.35, N=4
N = 4
p = .35
rate = N*p
# going out to 8 successes
k = np.arange(0,8)
poisson_trial_i = stats.poisson.pmf(k, rate)
# print poisson_trial_i

#plt.plot(k, poisson_trial_i, 'o-')
#plt.title ('Poisson: N = 4, p = .35')
#plt.xlabel('Number of successes')
#plt.ylabel('Probability of successes')
#plt.show()



# second trial with p=.35, N=40
N = 40
p = .35
rate = N*p
# going out to 30 successes
k = np.arange(0,30)
poisson_trial_ii = stats.poisson.pmf(k, rate)
# print poisson_trial_ii

#plt.plot(k, poisson_trial_ii, 'o-')
#plt.title ('Poisson: N = 40, p = .35')
#plt.xlabel('Number of successes')
#plt.ylabel('Probability of successes')
#plt.show()





# Gaussian Distribution Fits

# Binomial Data

# first trial with p=.35, N=4
N = 4
p = .35
# going out to 5 successes
k = np.arange(0,6)
binomial_trial_i = stats.binom.pmf(k, N, p)
# print binomial_trial_i

x = k
print(x)
y = binomial_trial_i
print(y)

# this is a trimmed mean
mean = 1
# print mean
sigma_squared = (((sum((x-mean)**2))/5))**.5
# print sigma_squared

def gaussian_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma_squared))
popt, pcov = curve_fit(gaussian_function,x,y,p0=[.384475, mean, sigma_squared])
plt.plot(x, gaussian_function(x,*popt))
plt.plot(k, binomial_trial_i, 'o-')
plt.title ('Binomial: N = 4, p = .35')
plt.xlabel('Number of successes')
plt.ylabel('Probability of successes')
plt.show()



# second trial with p=.35, N=40
N = 40
p = .35
# going out to 30 successes
k = np.arange(0,30)
binomial_trial_ii = stats.binom.pmf(k, N, p)
# print binomial_trial_ii

x = k
print(x)
y = binomial_trial_ii
print(y)

mean = sum(x)/30
# print mean
sigma_squared = (((sum((x-mean)**2))/29))**.5
# print sigma_squared

def gaussian_function(x, b, x0, sigma):
    return b*np.exp(-(x-x0)**2/(2*sigma_squared))
popt, pcov = curve_fit(gaussian_function,x,y,p0=[.1313, mean, sigma_squared])
plt.plot(x, gaussian_function(x,*popt))
plt.plot(k, binomial_trial_ii, 'o-')
plt.title ('Binomial: N = 40, p = .35')
plt.xlabel('Number of successes')
plt.ylabel('Probability of successes')
plt.show()


# Poisson Data

# first trial with p=.35, N=4
N = 4
p = .35
rate = N*p
# going out to 5 successes
k = np.arange(0,6)
poisson_trial_i = stats.poisson.pmf(k, rate)
# print poisson_trial_i

x = k
print(x)
y = poisson_trial_i
print(y)

# I used a trimmed mean
mean = 1
# print mean
sigma_squared = (((sum((x-mean)**2))/5))**.5
# print sigma_squared

def gaussian_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma_squared))
popt, pcov = curve_fit(gaussian_function,x,y,p0=[.384475, mean, sigma_squared])
plt.plot(x, gaussian_function(x,*popt))
plt.plot(k, poisson_trial_i, 'o-')
plt.title ('Poisson: N = 4, p = .35')
plt.xlabel('Number of successes')
plt.ylabel('Probability of successes')
plt.show()



# second trial with p=.35, N=40
N = 40
p = .35
rate = N*p
# going out to 30 successes
k = np.arange(0,30)
poisson_trial_ii = stats.poisson.pmf(k, rate)
# print poisson_trial_ii

x = k
print(x)
y = poisson_trial_ii
print(y)

mean = sum(x)/30
#print mean
sigma_squared = (((sum((x-mean)**2))/29))**.5
#print sigma_squared

def gaussian_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma_squared))
popt, pcov = curve_fit(gaussian_function,x,y,p0=[.105, mean, sigma_squared])
plt.plot(x, gaussian_function(x,*popt))
plt.plot(k, poisson_trial_ii, 'o-')
plt.title ('Poisson: N = 40, p = .35')
plt.xlabel('Number of successes')
plt.ylabel('Probability of successes')
plt.show()







