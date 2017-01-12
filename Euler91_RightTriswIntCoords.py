#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 22:45:53 2017

@author: christophergreen

Problem 91
The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin,
 O(0,0), to form ΔOPQ.


There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate 
lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.


Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?

"""
import itertools


def assemble(maxes):
    points=[]
    x=0;
    while x<=maxes:
        y=0
        while y<=maxes:
            points.append((x,y))
            y+=1
        x+=1
    points=points[1:] #to remove the origin itself
    #print("length of points is",len(points)) #= maxes^2-1

    combs=list(itertools.combinations(points,2))    
    #print("length of combs is",len(combs)) #= ((maxes^2-1)^2)/2
    trips=[]
    for comb in combs:
        a=(comb[0][0]**2+comb[0][1]**2)**.5
        b=(comb[1][0]**2+comb[1][1]**2)**.5
        c=((comb[0][0]-comb[1][0])**2+(comb[0][1]-comb[1][1])**2)**.5
        legs=[a,b,c]
        trips.append(legs)
      
    goods=[];
    print("there are: ",len(trips),"triangles to evaluate")
    for trip in trips:
        if round(trip[0]**2+trip[1]**2,10)==round(trip[2]**2,10) or round(trip[0]**2+trip[2]**2,10)==round(trip[1]**2,10) or round(trip[1]**2+trip[2]**2,10)==round(trip[0]**2,10):
            goods.append(trip) #if any arrangement of sides obeys Pythagorean, rounded to ten places, then good
    #print(goods)
    print("the number of right triangles that can be forms by using the origin and 2 lattice points with x and y max",maxes,"is:",len(goods))
    return

#assemble(2)    
#there are:  28 triangles to evaluate
#the number of right triangles that can be forms by using the origin and 2 lattice points with x and y max 2 is: 14

#assemble(10)
#there are:  7140 triangles to evaluate
#the number of right triangles that can be forms by using the origin and 2 lattice points with x and y max 10 is: 448

#assemble(20)
#there are:  96580 triangles to evaluate
#the number of right triangles that can be forms by using the origin and 2 lattice points with x and y max 20 is: 1986

#assemble(30)
#there are:  460320 triangles to evaluate
#the number of right triangles that can be forms by using the origin and 2 lattice points with x and y max 30 is: 4764

#assemble(40)
#there are:  1410360 triangles to evaluate
#the number of right triangles that can be forms by using the origin and 2 lattice points with x and y max 40 is: 8826

#assemble(50) --> 14234
#there are:  3378700 triangles to evaluate
#the number of right triangles that can be forms by using the origin and 2 lattice points with x and y max 50 is: 14234