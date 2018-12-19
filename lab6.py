from turtle import Turtle
import turtle
import random
'''
colors = ["red", "blue", "yellow"]
class Square(Turtle):
	def __init__(self, size, shape = turtle.shape("Square") ):
		
		self.size = size

	
	def random_color(self):
		color = random.choice(colors)
		turtle.color(color)	

c = Square(15)
c.random_color()

'''
class Hexagon(Turtle):
	def __init__(self, size, speed, color=turtle.color("red")):
		self.size = size
		self.speed = speed
		

	def create_hexagon(self): 
		turtle.forward(100)
		turtle.right(60)
		turtle.speed(10)
		

hexagongon = Hexagon(100, 0, "red")

hexagongon.create_hexagon()
hexagongon.create_hexagon()
hexagongon.create_hexagon()
hexagongon.create_hexagon()
hexagongon.create_hexagon()
hexagongon.create_hexagon()


turtle.mainloop()