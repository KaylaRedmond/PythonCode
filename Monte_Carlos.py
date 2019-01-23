import math
import numpy as np
import scipy
import scipy.integrate
import matplotlib.pyplot as plt
import time





# Box Mueller Method
# take independent random variables x1,x2 that are uniformally distributed
# in interval (0,1)

time_start = time.process_time()
x1 = np.random.random(10000)
x2 = np.random.random(10000)
#plt.hist(x1,bins=30)
#plt.show()

# form new independent variables that have a standard normal distribution
# with mean = 0, sigma = 1

def gaussiandist(x1,x2):
    z1 = np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)
    z2 = np.sqrt(-2*np.log(x1)) * np.sin(2*np.pi*x2)
    return z1,z2

z1,z2 = gaussiandist(x1,x2)

time_elapsed = (time.process_time() - time_start)
print(time_elapsed)


# this is a normal standard distribution to compare to the randomly generated distribution
mu = 0.0
sigma = 1.0
f = lambda x: np.exp((-(x-mu)**2)/(2*sigma**2))/np.sqrt(2*np.pi*sigma**2)
xnormal = np.arange(-4,4,.01)
ynormal = f(xnormal)


plt.hist(z1,bins=30,normed=1)
plt.plot(xnormal,ynormal, 'o-')
plt.title('Box Mueller Distribution $z_1$')
plt.xlabel('$z_1$')
plt.ylabel('Frequency')
plt.legend(('PDF','Samples'))
plt.show()

plt.hist(z2,bins=30,normed=1)
plt.plot(xnormal,ynormal, 'o-')
plt.title('Box Mueller Distribution $z_2$')
plt.xlabel('$z_2$')
plt.ylabel('Frequency')
plt.legend(('PDF','Samples'))
plt.show()

#plt.scatter(z1,z2)
#plt.xlabel('z1')
#plt.ylabel('z2')
#plt.show()










# von Neumann Method
# this is an acceptance-rejection technique
# take my normal distribution and create a uniform random distribution of x values
# between -10 and 10, so as to cover a 10sigma range in regards to the gaussian;
# then, given the random distribution of x values, I also form a normal random distribution
# of y values between 0 and the height of my gaussian;
# evaluate the Gaussian at each x value, and if the gaussian is above the randomly generated
# y value I keep the random x and random y value


time_start = time.process_time()

mu = 0.0
sigma = 1.0
f = lambda x: np.exp((-(x-mu)**2)/(2*sigma**2))/np.sqrt(2*np.pi*sigma**2)

#x = np.arange(-4,4,.01)
#y = f(x)
#plt.plot(x,y)
#plt.show()


xvalues = []
yvalues = []
n = 10000
for i in range(n):
    x = np.random.uniform(-10,10)
    #print x
    y = np.random.uniform(0,f(0))
    #print y
    if f(x)>=y:
        xvalues.append(x)
        yvalues.append(y)

# all accepted points within probability distribution are uniformly distributed


#print xvalues

time_elapsed = (time.process_time() - time_start)
print(time_elapsed)

#plt.scatter(xvalues,yvalues)
plt.hist(xvalues,bins=30,normed=1)
plt.plot(xnormal,ynormal, 'C1', linewidth=5.0)
plt.title('Von Neumann Distribution')
plt.ylabel('Frequency')
plt.xlabel('x')
plt.legend(('PDF','Samples'))
plt.show()










# Metropolis Method
# random walk method

time_start = time.process_time()

mu = 0.0
sigma = 1.0
f = lambda x: np.exp((-(x-mu)**2)/(2*sigma**2))/np.sqrt(2*np.pi*sigma**2)


n = 10000
# Choosing a random number from -1,1, doing so 10,000 times
delta = np.random.uniform(-1,1,n)

x = 0.

# this is the empty set that will hold my x values
vec = []
vec.append(x)

for i in range(1,n):
    # trial value is initial value plus a "random walk"
    trial = x + delta[i]
    # weight function is pdf(trial)/pdf(xvalue)
    weight = f(trial)/f(x)
    

    
    rprob = np.random.uniform(0,1)

    # accept the trial if the weight is greater than 1 or accept it with a random probability
    # between 0 and 1
    if weight >= 1 or rprob <= weight:
        x = trial
        vec.append(x)
        


time_elapsed = (time.process_time() - time_start)
print(time_elapsed)

plt.hist(vec, bins=30,normed=1)
plt.plot(xnormal,ynormal,'ro')
plt.title('Metropolis Method')
plt.ylabel('Frequency')
plt.xlabel('x')
plt.legend(('PDF','Samples'))
plt.show()










# C Code
# this is the code given in Homework Set 4


time_start = time.process_time()

n = 12
g = 0.0

xvalues = []
xvaluessquared = []

# I am running the code 10000 times

for m in range(10000):
    g = 0.0
    for i in range(0,n,1):
        g = g + np.random.uniform(0,1)

    x = g - n/2.
    xvalues.append(x)
    xvaluessquared.append(x**2)
    #print x


time_elapsed = (time.process_time() - time_start)
print(time_elapsed)

plt.hist(xvalues,bins=30,normed=1)
plt.plot(xnormal,ynormal, 'C1', linewidth=5.0)
plt.title('Algorithm Method')
plt.ylabel('Frequency')
plt.xlabel('x')
plt.legend(('PDF','Samples'))
plt.show()


# 1st Moment for C Code:
#mean = (1/10000)*sum(xvalues)
#print(mean)


# 2nd Moment for C Code:
#standarddev = ((1/(10000-1))**(1/2))*((sum(xvaluessquared)))**(1/2)
#print(standarddev)

# The standard deviation for the C Code provided is 1.0, as we expected


    


# I am overplotting a standard normal Gaussian distribution to demonstrate
# that each model generates a Gaussian distribution
    

# I also ran the times it took to compute each method
#  Box - .00088 sec
#  Van Neumann - .0654 sec
#  Metropolis - .0922 sec
#  C Code - .105 sec

# it makes sense that the Box method took the shortest time because it was using
# numpy functions.  The other three methods took longer because they were doing for loops
# 10000 times each, so they would naturally take longer to do.









