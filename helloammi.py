#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 12:54:32 2021

@author: shaikmohammadasrarahammad
"""

import turtle
mypen = turtle.Turtle()
mypen.shape('turtle')
mypen.speed(10)
window = turtle.Screen()
window.bgcolor('skyblue')
style = ('Courier', 50, 'italic')
rainbow = ['red', 'orange','green','blue','indigo','violet']
size = 200
mypen.penup()
mypen.goto(0, -80)
for color in rainbow:
    mypen.color(color)
    mypen.fillcolor(color)
    mypen.begin_fill()
    mypen.circle(size)
    mypen.end_fill()
    size -=30
mypen.penup()
mypen.color('white')
mypen.goto(0, -150)
mypen.write("Hello Ammi",font=style, align='center')
mypen.penup()
mypen.hideturtle()
turtle.done()