import turtle
import random

my_turtle = turtle.Turtle()


turtle.Screen().bgcolor("yellow")
colours = ["red", "cyan", "blue", "purple"]

my_turtle.color('red')

def square(length, angle):
	for i in range(4):
		my_turtle.forward(length)
		my_turtle.right(angle)

for i in colours:
    my_turtle.color(random.choice(colours))



for i in range(40):
	square(110,90)
	my_turtle.right(10)