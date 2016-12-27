# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:33:30 2016

@author: Nabin
"""
#Given mass1, mass2 and distance, calculate force assuming Gravitational Constant is 1
list1 = [(250,600,50), (600,870,99),(745,645,58),(980,450,25),(854,600,89)]

forceCalulated = []
def forceCalculation(x):
    for m1,m2,d in list1:       
        forceCalulated.append((m1*m2)/(d*d))
    return forceCalulated
    #return [(m1*m2)/(d*d) for m1,m2,d in x]

forces = forceCalculation(list1)  
print "The calculated Forces are: ", forces
      