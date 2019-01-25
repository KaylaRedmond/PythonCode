import math
import numpy as np
import scipy
import matplotlib.pyplot as plt


# make a matrix of the 3D data for the two hypotheses
f_0 = np.matrix(((0,1,5),(1,2,6),(2,3,4),(3,3,7),(4,5,6),(5,5,5)))
print(f_0)
f_1 = np.matrix(((1,0,4),(2,1,3),(3,1,5),(3,2,4),(5,3,4),(6,5,6)))
print(f_1)





# find mean
mu_0 = np.mean(f_0,axis=0)
print(mu_0)

mu_1 = np.mean(f_1,axis=0)
print(mu_1)


# find covariance
# np.cov finds covariance matrix
# we set rowvar = False, which means that each column represents a variable
# and each row is an observation
cov_0 = 5*np.cov(f_0,rowvar=False)
print(cov_0)

cov_1 = 5*np.cov(f_1,rowvar=False)
print(cov_1)





# W is the sum of the covariance matrices
W = cov_0 + cov_1
#print(W)


# take inverse of W given that W is a square matrix/array
W_inv = np.linalg.inv(W)
#print(W_inv)





# calculate the coefficients a
# .T takes the transpose
a = W_inv*(mu_0-mu_1).T
print(a)





# mean test statistic
tau_0 = np.dot(a.T,mu_0.T)
print(tau_0)

tau_1 = np.dot(a.T,mu_1.T)
print(tau_1)





# covariance for test statistic
sig_0 = a.T*cov_0*a
print(sig_0)

sig_1 = a.T*cov_1*a
print(sig_1)





# calculate g vectors
g_0 = a.T*f_0.T
print(g_0)

g_1 = a.T*f_1.T
print(g_1)





# Plot normal distribution with tau as mean and sigma as standard deviation
tau_0 = 1.7594
tau_1 = -0.2616
sig_0 = 0.7798
sig_1 = 1.241

mu_0 = tau_0
sigma_0 = np.sqrt(sig_0)
mu_1 = tau_1
sigma_1 = np.sqrt(sig_1)
normaldist_0 = lambda x: np.exp((-(x-mu_0)**2)/(2*sigma_0**2))/np.sqrt(2*np.pi*sigma_0**2)
normaldist_1 = lambda x: np.exp((-(x-mu_1)**2)/(2*sigma_1**2))/np.sqrt(2*np.pi*sigma_1**2)

xnormal = np.arange(-7,7,.01)
ynormal_0 = normaldist_0(xnormal)
ynormal_1 = normaldist_1(xnormal)

plt.plot(xnormal,ynormal_0,'o-')
plt.plot(xnormal,ynormal_1,'o-')
plt.legend(('Globular','Open'))
plt.xlabel('t')
plt.show()





# Significance level = alpha = integral of H0 from t = 1 out to ~ t = 10
xnormal_int = np.arange(1,10,.01)
ynormal_0int = normaldist_0(xnormal_int)
print(np.trapz(ynormal_0int,xnormal_int,dx=.05))


# Power of the test = 1-beta = integral of H1 from ~ t = -10 to t = 1
xnormal_int = np.arange(-10,1,.01)
ynormal_1int = normaldist_1(xnormal_int)
beta = np.trapz(ynormal_1int,xnormal_int,dx=.05)
print(1-beta)

