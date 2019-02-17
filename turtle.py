import turtle
import random

my_turtle = turtle.Turtle()


turtle.Screen().bgcolor("yellow")
colours = ["red", "cyan", "blue", "purple", "white", "orange"]


def square(length, angle):
	for i in range(4):
		pick_color = random.choice(colours)
		my_turtle.color(pick_color)
		my_turtle.forward(length)
		my_turtle.right(angle)


for i in range(40):
	square(110,90)
	my_turtle.right(10)