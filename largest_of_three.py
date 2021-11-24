#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:54:10 2021

@author: shaikmohammadasrarahammad
"""

a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
c = int(input("Enter c value:"))
if(a>b):
    if(a>c):
        print(a,",a is the largest number")
else:
    if(b>c):
        print(b,",b is the largest number")
    else:
        print(c,",c is the largest number")