import turtle
from turtle import Turtle
import math



class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		self.color(color)
		self.shape("circle")
		self.shapesize(r/10)
		self.penup()
		self.goto(x,y)
	def move(self, SCREEN_WIDTH, SCREEN_HEIGHT):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		up_side_ball = new_y + self.r
		down_side_ball = new_y - self.r
		self.goto(new_x,new_y)
		if SCREEN_HEIGHT<=up_side_ball:
			self.dy = -self.dy
		elif -SCREEN_HEIGHT >= down_side_ball:
			self.dy = -self.dy
		elif -SCREEN_WIDTH >= left_side_ball:
			self.dx = -self.dx
		elif SCREEN_WIDTH <= right_side_ball:
			self.dx = -self.dx

	
