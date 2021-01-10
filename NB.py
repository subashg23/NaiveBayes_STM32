# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 20:17:23 2021

@author: Subash
"""

from sklearn.naive_bayes import GaussianNB
import random
import numpy as np
import math
NBVECS = 3
VECDIM = 2
ballRadius = 1.0
print(np.random.randn())
x1 = [1.5, 1] +  ballRadius * np.random.randn(NBVECS,VECDIM)
x2 = [-1.5, 1] + ballRadius * np.random.randn(NBVECS,VECDIM)
x3 = [0, -3] + ballRadius * np.random.randn(NBVECS,VECDIM)

#x1 = [1.5, 1] +  ballRadius * [2.8,1.1]
#x2 = [-1.5, 1] + ballRadius * [1.3,2.2]
#x3 = [0, -3] + ballRadius * [2.6,3.8]

# All points are concatenated
print("X1 :",x1)
print("X2 :",x2)
print("X3 :",x3)
X_train=np.concatenate((x1,x2,x3))

# The classes are 0,1 and 2.
Y_train=np.concatenate((np.zeros(NBVECS),np.ones(NBVECS),2*np.ones(NBVECS)))
gnb = GaussianNB()
print("x= ",X_train)
print("y= ",Y_train)
gnb.fit(X_train, Y_train)
y_pred = gnb.predict([[1.5,1.0]])
print(y_pred)
print("Parameters")
# Gaussian averages
print("Theta = ",list(np.reshape(gnb.theta_,np.size(gnb.theta_))))

# Gaussian variances
print("Sigma = ",list(np.reshape(gnb.sigma_,np.size(gnb.sigma_))))

# Class priors
print("Prior = ",list(np.reshape(gnb.class_prior_,np.size(gnb.class_prior_))))

print("Epsilon = ",gnb.epsilon_)

print("ypredction = ",y_pred)