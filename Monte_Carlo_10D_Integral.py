import math
import numpy as np
import scipy
import scipy.integrate
import matplotlib.pyplot as plt



def samplemean(m):
    f_total = 0.0
    for i in range(m):
        a = np.random.random()
        b = np.random.random()
        c = np.random.random()
        d = np.random.random()
        e = np.random.random()
        l = np.random.random()
        g = np.random.random()
        h = np.random.random()
        j = np.random.random()
        k = np.random.random()
        mult_integral = (a+b+c+d+e+l+g+h+j+k)**2
        #print mult_integral

        f_total += mult_integral
    return f_total/m
#print samplemean(128)


error_vs_samplesize = []
for i in range(1,15):
    m = 2**i
    t = samplemean(m)
    error = abs((samplemean(m)-float((155.0/6.0)))/float(155.0/6.0))
    error_vs_samplesize.append(error)
    print((m,float(1.0/(m**(0.5))),t,error))


#print error_vs_samplesize

errorlist = []
for i in range(1,15):
    m = 2**i
    errorlist.append(float(1.0/(m**(0.5))))

#print errorlist
   

plt.plot(errorlist, error_vs_samplesize)
plt.xlabel('1/Sqrt(n)')
plt.ylabel('Error')
plt.title('Error vs. Sample Size')
plt.show()


