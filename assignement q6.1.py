#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:24:30 2020

@author: adamdrake
"""


#6a
clf()
x,y = loadtxt("skydive.txt",unpack = True)
plot(x,y,"g")
title("Graph to show height against time for a skydiver")
xlabel("time(s)")
ylabel("height(m)")
print()
#6bi
print("I beleive the skydiver reachers terminal velocity between 7 and 9 seconds as this is when the graph starts to become straight")
print()
#6bii
print("I believe the time at which the skydiver releases her parachute is around 25 seconds as this is when the height decreased is much less than before")
print()
#6c