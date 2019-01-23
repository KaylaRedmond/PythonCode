import math
import numpy as np
import scipy
import scipy.integrate
import matplotlib.pyplot as plt



f = lambda x: np.exp(-x)
x = np.arange(0,1,.01)
y = np.exp(-x)

plt.plot(x,y, 'o-')
plt.title ('e$^{-x}$')
plt.xlabel ('x')
plt.ylabel ('e$^{-x}$')
plt.show()


def trapezoidal(f, a, b, n):
    # h is the size of the intervals
    h = float(b - a) / float(n)
    T = 0.0
        
    for i in range(0, n):
        # += means that it adds and continually updates the def of T
        T += (h*(f(a + i*h) + f(a + (i+1)*h)))/2
    return T


error_table = []
for i in range(0,10):
    n = 2**i
    t = trapezoidal(f, 0, 1, n)
    error = abs((trapezoidal(f, 0, 1, n)-.63212)/.63212)
    error_table.append([error])
    print((n, 1.0/n, t, error))

stepsize_table = []
for i in range(0,10):
    n = 2**i
    stepsize_table.append([1.0/n])
    


plt.loglog(stepsize_table,error_table)
plt.xlabel('Step Size')
plt.ylabel('Error')
plt.title('Error vs. Step Size Trapezoidal')
plt.show()




def romberg(f, a, b):
    h = float(b - a)
    R = 0.0

    for i in range(1,10):
        n = 2**i
        R00 = (1.0/2.0)*h*(f(a) + f(b))
        
        R01 = 0.5*R00 + (1.0/2.0)*h*(f(a+h*1.0/2.0))
        R11 = (4.0*R01-R00)/3.0
        ep1 = abs(R11 - R00)

        R02 = 0.5*R01 + (1.0/(2.0**2.0))*h*(f(a+h*1.0/(2.0**2.0)) + + f(a+h*3.0*(1.0/(2.0**2.0))))
        R12 = (4.0*R02-R01)/3.0
        R22 = ((4.0**2.0)*R12-R11)/((4.0**2.0) - 1.0)
        ep2 = abs(R22 - R11)

        R03 = 0.5*R02 + (1.0/(2.0**3.0))*h*(f(a+h*1.0/(2.0**3.0)) + + f(a+h*3.0*(1.0/(2.0**3.0))) + f(a+h*5.0*(1.0/(2.0**3.0)))+f(a+h*7.0*(1.0/(2.0**3.0))))
        R13 = (4.0*R03-R02)/(3.0)
        R23 = ((4.0**2.0)*R13-R12)/((4.0**2.0) - 1.0)
        R33 = ((4.0**3.0)*R23-R22)/((4.0**3.0) - 1.0)
        ep3 = abs(R33 - R22)

        error00 = abs((R00-.63212)/.63212)
        error11 = abs((R11-.63212)/.63212)
        error22 = abs((R22-.63212)/.63212)
        error33 = abs((R33-.63212)/.63212)
        

    return [[R00,error00],[R01,R11,error11],[R02,R12,R22,error22],[R03,R13,R23,R33,error33]]


print(romberg(f, 0.0, 1.0))




def hitormiss(f, a, b, n):
    # n is the number of evaluation points
    # H is the height of the rectangular area
    Area = f(a) * (b-a)
    #print Area
    N_successes = 0.0
    for i in range(n):
        x = np.random.random()
        #print x
        y = np.random.uniform(0,f(a))
        #print y
        #print f(x)
        if f(x)>=y:
            N_successes += 1
    return Area*(N_successes/n)

#print hitormiss(f,0,1,1000)

error_hitormiss = []
hitormiss_list = [10,20,50,100,200,500,1000,2000,5000,10000]
for x in hitormiss_list:
    t = hitormiss(f, 0, 1, x)
    error = abs((hitormiss(f, 0, 1, x)-.63212)/.63212)
    error_hitormiss.append([error])
    print((x, t, error))

n_table = [10,20,50,100,200,500,1000,2000,5000,10000]


plt.loglog(n_table,error_hitormiss)
plt.xlabel('n')
plt.ylabel('Error')
plt.title('Error vs. n Hit or Miss')
plt.show()




