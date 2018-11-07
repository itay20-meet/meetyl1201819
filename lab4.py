x=5
class animal():
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("Yummy " +self.name +"is eating " + food)
	def description(self):
		print(self.name + "is" + self.age +"years old and loves the color" + self.favorite_color)
	def make_sound(self, sound):
		print(sound*x)
animal = animal("moo", "otis", "11", "white")
#animal.eat("burger")
#animal.description()
animal.make_sound("moo")
class person():
	def __init__(self,name,age,hight,city,gender, favorite_breakfast):
		self.name = name
		self.age = age
		self.hight = hight
		self.city = city
		self.gender = gender
		self.favorite_breakfast = favorite_breakfast
	def eat_breakfast(self, favorite_breakfast):
		print(self.name + "is eating" + self.favorite_breakfast )	
itay = person("Itay","15", "171", "Jerusalem", "male", "eggs")
itay.eat_breakfast()

