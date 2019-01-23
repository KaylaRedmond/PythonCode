import math
import numpy as np
import scipy
import scipy.integrate
import matplotlib.pyplot as plt





# this is the first function f(x)
f = lambda x: (x**(3/2))*np.exp(-x)
x = np.arange(0,3,.01)
y = f(x)

plt.plot(x,y, 'o-')
plt.title ('f(x) = $x^{3/2} e^{-x}$')
plt.xlabel ('x')
plt.ylabel ('f(x)')
plt.show()


# this is f(x)/w(x) where w(x) is the importance function
x = np.arange(0,3,.01)
y = f(x)/(np.exp(-x))

plt.plot(x,y, 'o-')
plt.title ('f(x)/w(x)')
plt.xlabel ('x')
plt.ylabel ('f(x)/w(x)')
plt.show()



def samplemean(n):
    f_total = 0.0
    for i in range(n):
        # choosing a random number between 0 and 1
        a = np.random.uniform()

        # this is the integral f(x(y))/w(x(y))
        integral = ((math.log(1/(1-a)))**(3/2))
        #print integral

        # you then add the evaluations of the integral
        f_total += integral
    return f_total/n
print(samplemean(2000))










# new f(x)
f = lambda x: 1/(x**2 + (np.cos(x))**2)
x = np.arange(0,np.pi,.01)
y = f(x)

plt.plot(x,y, 'o-')
plt.title ('f(x) = 1/($x^2 + cos^2x$)')
plt.xlabel ('x')
plt.ylabel ('f(x)')
plt.show()


# f(x)/w(x)
x = np.arange(0,np.pi,.01)
y = f(x)/(np.exp(-x))

plt.plot(x,y, 'o-')
plt.title ('f(x)/w(x)')
plt.xlabel ('x')
plt.ylabel ('f(x)/w(x)')
plt.show()


n = 200

# given range of a values, we can calculate required A
a = np.arange(0.1,2.0,0.1)
A = lambda a: a*(1-np.exp(-a*np.pi))**(-1)
#print a
#print A(a)


# first I need to find the variance of the Monte Carlo data
# and use that to optimize a

for a in np.arange(0.1,2.0,0.1):
    integralvalues = []
    f_total = 0.0
    A = a*(1-np.exp(-a*np.pi))**(-1)
    for i in range(n):
        y = np.random.uniform()
        # this is the integral f(x(y))/w(x(y))
        integral = f((1/a)*(np.log((A/a)/(A/a - y))))/(A*np.exp(-np.log((A/a)/(A/a - y))))
        #print integral
        integralvalues.append(integral)

        # you then add the evaluations of the integral
        f_total += integral
        

        
        # to minimize a I need to find the variance of the "integral"     
    # 1st Moment
    mean = f_total/n
    #print mean

    # 2nd Moment
    #print integralvalues
    #print sum(integralvalues)
    standarddev = ((1./(n-1.))**(1./2.))*((sum((integralvalues-mean)**2.))**(1./2.))
    print(a,standarddev**2.)
    #print(standarddev**2.)
    

# I find the variance to be minimized at a = 0.8
# I can now resolve the integral with a = 0.8


def samplemean(n):
    f_total = 0.0
    for i in range(n):
        a = 0.8
        A = a*(1-np.exp(-a*np.pi))**(-1)
        # choosing a random number between 0 and 1
        y = np.random.uniform()

        # this is the integral f(x(y))/w(x(y))
        integral = f((1/a)*(np.log((A/a)/(A/a - y))))/(A*np.exp(-np.log((A/a)/(A/a - y))))
        #print integral

        # you then add the evaluations of the integral
        f_total += integral
    return f_total/n
print(samplemean(2000))



