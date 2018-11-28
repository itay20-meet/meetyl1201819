from turtle import *
import random
import math
class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

ball = [0,0,3,4,7]
ball2  =[1,1,3,4,6]

def check_collision(ball, ball2):
	D = math.sqrt(math.pow((1-0),2) + math.pow((1-0),2))
	print (D)
	if D<7+6:
		print("yes!")
	else:
		print("no!")

check_collision(ball, ball2)

balls = []
balls.append(ball)
balls.append(ball2)
print(balls)