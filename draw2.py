# Turtle Drawing
# Description: Drawing inspired from the painting - The Son of Man by Rene Magritte
# Author: Vatsal Parmar
# Date: 27th June 2019

import turtle
from turtle import *

#################################### Setting up the turtle #################################### 

v = turtle
canvas = Screen()
colors = ["red", "orange", "blue", "black", "gold", "skyblue", "navy", "brown", "grey", "cyan", "green", "white"]

#################################### setting up Functions #################################### 

def movePos(length):
  v.penup()
  v.forward(length)
  v.pendown()
  return

def changeCoord(x, y):
  v.penup()
  v.goto(x,y)
  v.pendown()
  return

def changeWidth(width):
  v.pensize(width)
  return

def square(side, colour):
    v.pencolor(colour)
    v.pensize()
    for i in range(4):
        v.forward(side)
        v.left(90)
    return

def rectangle(side1, side2, lineColour, filledColour="none"):
    # yellow rectangle - filled with violet
    v.pencolor(lineColour)
    if filledColour != "none" :
        v.fillcolor(filledColour)
        v.begin_fill()
    for i in range(2):
        v.forward(side1)
        v.right(90)
        v.forward(side2)
        v.right(90)
    if filledColour != "none" :
        v.end_fill()
    return

def dottedLine(radius, length):
  for h in range(length):
    v.dot(radius)
    movePos(radius)
  return  

def rightWave(radius, length):
  for g in range(length//2):
    v.dot(radius)
    v.right(5)
    movePos(radius-2)
  return

def leftWave(radius, length):
  for g in range(length//2):
    v.dot(radius)
    v.left(5)
    movePos(radius-2)
  return

def tie(length):
  v.pencolor(colors[0])
  for x in range(20):
    changeWidth(x)
    v.forward(length/20)
  return

#################################### Main part #################################### 

v.speed(20)
changeCoord(-250, 300)
rectangle(500, 350, colors[3], colors[-1])


changeCoord(-250, 150)
rectangle(500, 125, colors[2], colors[5])

changeCoord(-250, 25)
rectangle(500, 75, colors[3], colors[8])

changeCoord(-250, 300)
rectangle(500, 150, colors[3], colors[-1])

#################################### Creating the person #################################### 

changeCoord(-25, -40)
v.seth(90)
changeWidth(20)
rectangle(250, 75, colors[3], colors[3])

#################################### Drawing Arms #################################### 

changeCoord(-25, 210)
v.seth(180)
v.left(75)
v.forward(150)

changeCoord(50, 210)
v.seth(0)
v.right(75)
v.forward(150)

#################################### Creating the Head #################################### 

changeCoord(-5, 230)
v.color(colors[3])
v.begin_fill()
v.circle(20)
v.end_fill()

#################################### Creating the Red tie #################################### 

changeCoord(15, 210)
v.seth(-90)
v.pencolor(colors[0])
tie(100)

#################################### Drawing the green apple #################################### 

changeCoord(5, 240)
changeWidth(10)
v.color(colors[10])
v.begin_fill()
v.circle(10)
v.end_fill()

#################################### Creating a branch for the apple #################################### 

changeCoord(15, 250)
v.seth(90)
v.pencolor(colors[10])
v.forward(10)
v.right(45)
v.forward(15)
v.backward(15)
v.left(90)
v.forward(15)

#################################### Waves Shapes #################################### 

changeCoord(-240, 290)
v.seth(0)
v.pensize(5)
v.pencolor(colors[3])
rightWave(10, 15)
leftWave(10, 15)

changeCoord(240, 290)
v.seth(180)
v.pencolor(colors[4])
leftWave(10, 15)
rightWave(10,15)

changeCoord(-150, 250)
v.seth(0)
v.pencolor(colors[6])
rightWave(10, 15)
leftWave(10,19)

changeCoord(150, 250)
v.seth(180)
v.pencolor(colors[7])
leftWave(10, 15)
rightWave(10,15)

#################################### End of Drawing #################################### 

v.penup()
v.home()
v.exitonclick()

#################################### End #################################### 
