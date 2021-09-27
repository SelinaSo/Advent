# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:14:37 2021

@author: selin
"""


f = open("input_1.txt", "r")
a = (f.read()).split("\n")
len(a)
a = a[:-2]

## Part one
x = 0


for i in a:
    for j in a:
        if (int(float(i)) + int(float(j)) == 2020):
             while(x==0):   
                print(i, j)
                print(int(i) * int(j))
                x = 1
             break

## Part two
y = 0

for i in a:
    for j in a:
        for k in a:
            if (int(float(i)) + int(float(j)) + int(float(k)) == 2020):
                while(y==0):
                    print(i, j, k)
                    print(int(i) * int(j) * int(k))
                    y = 1
                break