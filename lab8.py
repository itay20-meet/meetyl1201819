from turtle import *
import random
import math
class Ball(Turtle):
	def __init__(self, x, y, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

ball = Ball(0, 0, 7, "blue", "fast")
ball2  = Ball(1, 1, 6, "red", "normal" )

def check_collision(ball, ball2):
	D = math.sqrt(math.pow((ball2[0]-ball[0]),2) + math.pow((ball2[1]-ball[1]),2))
	print (D)
	if D<ball[2]+ball2[2]:
		print("yes!")
	else:
		print("no!")

check_collision(ball, ball2)

balls = []
balls.append(ball)
balls.append(ball2)
print(balls)