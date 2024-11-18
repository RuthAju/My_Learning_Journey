import turtle
from turtle import *
import random

class Triangle:    
    def __init__(self):
        self.shape = shape("turtle")
        # Set up turtle environment
        screen = turtle.Screen()
        screen.bgcolor((self.random_color()))
        screen.title("Random Triangle generation")
        root = screen._root
        root.iconbitmap(default="")

    def random_color(self):
        return (random.random(), random.random(), random.random())
        
    def triangle(self):
        turtle.begin_fill()

        # Set the color before putting the pen down
        turtle.color(self.random_color())

        for _ in range(3):
            # Set pen size once before drawing
            turtle.pensize(4)

            # Start drawing only after setting the color
            turtle.pendown()
            turtle.forward(100)
            turtle.right(120)
        turtle.end_fill() 
        turtle.penup() 

    def run(self):
        # Draw multiple triangles
        for x in range(4):
            self.triangle()
            # Adjust position for each triangle
            turtle.goto(-50, 200 - (x+1) * 100)

        turtle.hideturtle()
        turtle.done()

# Lifts the pen after drawing the triangle
turtle.penup()

# Sets the initial position for the first triangle
turtle.setposition(-50, 200)

if __name__ == "__main__":
    tri = Triangle()
    tri.run()

# def Square():
# turtle.penup()
# turtle.setpos(-50, 200)
# turtle.begin_fill()
# for _ in range(4):
#     turtle.pensize(4)
#     turtle.pendown()
#     turtle.forward(100)
#     turtle.right(90)
#     # turtle.color(random_color())

# turtle.end_fill()
# turtle.penup()


# Hexagon
# turtle.penup()
# turtle.setpos(-50, 200)
# turtle.begin_fill()
# for _ in range(16):
#     turtle.pensize(4)
#     turtle.pendown()
#     turtle.forward(100)
#     turtle.right(22.5)
#     # turtle.color(random_color())

# turtle.end_fill()
# turtle.penup()


# Rectangle
# turtle.penup()
# turtle.setpos(-70, 20)
# turtle.begin_fill()
# turtle.pensize(4)
# turtle.pendown()
# turtle.forward(140)
# turtle.right(90)
# turtle.forward(70)
# turtle.right(90)
# turtle.forward(140)
# turtle.right(90)
# turtle.forward(70)
# turtle.right(90)

# turtle.end_fill()
# turtle.penup()



turtle.done()
