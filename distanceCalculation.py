# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:54:25 2016

@author: Nabin
"""

#velocity and time is given, calculate distance and then convert that distance into miles and feet

data = [(250,10), (350,60), (780,45)]

def calculateDistance(x):
    return  [v*t for v,t in x ]

distance = calculateDistance(data)

print "The calculated distance is: ", distance
print "The distance in miles: ",[round(value/1609.0,2) for value in distance]
print "The distance in feet: ", [value*1.54 for value in distance]
