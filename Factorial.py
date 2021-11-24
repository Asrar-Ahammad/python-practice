#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 21:59:38 2021

@author: shaikmohammadasrarahammad
"""

print("\nEnter a number to find factorial")
num=int(input("Enter the number :"))
factorial=1
if(num<0):
    print("The factorial donot exist")
elif(num==0):
    print("The factorial of 0 is 1")   
else:
    for i in range(1,num+1):
        factorial=factorial*i
print("\nThe factorial of",num,"is",factorial)
    