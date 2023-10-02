from turtle import Turtle, Screen
import random

t = Turtle()
screen=Screen()
screen.colormode(255)
def color_generator():
	return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

directions= [0,90,180,270]
t.pensize(10)
# for i in range(15):
# 	t.forward(10)
# 	t.penup()
# 	t.forward(10)
# 	t.pendown()

for i in range(20):
	t.color(color_generator())
	t.forward(20)
	t.setheading(random.choice(directions))

screen.exitonclick()
