import turtle
import random

t = turtle.Turtle()

colors = ['medium spring green','dark slate gray','light steel blue','medium purple','orchid','goldenrod','salmon']
directions= [0,90,180,270]

# for i in range(15):
# 	t.forward(10)
# 	t.penup()
# 	t.forward(10)
# 	t.pendown()

for i in range(300):
	t.color(random.choice(colors))
	t.forward(20)
	t.setheading(random.choice(directions))
