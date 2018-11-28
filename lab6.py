from turtle import Turtle
import turtle
import random

colors = ["red", "blue", "yellow"]
class Square(Turtle):
	def __init__(self, size, shape = turtle.shape("Square") ):
		
		self.size = size

	
	def random_color(self):
		color = random.choice(colors)
		turtle.color(color)	

c = Square(15)
c.random_color()
turtle.mainloop()

