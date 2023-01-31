#proj02 by Sayem Lincoln
"""
Created on Wed Jan 18 16:33:35 2017
@author: srlin
"""
# x, y and length are variables
x=-220
y= 220
length=440
# importing turtle, time and random
import turtle
import time
import random
#picking color
def pick_color():
    colors = ["blue","black","brown","red","yellow","green","orange","beige","turquoise","pink"]
    random.shuffle(colors)
    return colors[0]

print("Look for the Python Turtle Graphics window")
print("Position it and the Python Shell window side by side.")
input("Then press `Enter' to continue ...")
i = int(input("Enter the number of squares to be printed:"))
print()

if i<=0 or i>=11:
        print("Wrong Integer. Input integer between 1 to 10.")
        print("Try Again.")
else:
    for z in range (i):
        x=x+20
        y=y-20
        length-=40
        #z +=2
        print("Length of one side of square", z , ":" ,length,)
        turtle.up()
        turtle.goto(x,y)
        turtle.color(random.random(),random.random(),random.random())
        turtle.begin_fill()
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.end_fill()    
        turtle.up()
        time.sleep(1)
        print("Square" , z , "is printed")
        print()
print("Thank You for playing.")
time.sleep(4)
turtle.bye()

# Questions
#Q1: 7
#Q2: 1
#Q3: 1
#Q4: 7

