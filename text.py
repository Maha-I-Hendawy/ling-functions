class Text:
	def __init__(self, text):
		self.text = text 

	
	def words(self):
		return self.text.split()


	def sents(self):
		return self.text.split('.')



class Person:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name 

	def __repr__(self):
		return f"{self.first_name}, {self.last_name}"



class Customer(Person):
	def __init__(self, first_name, last_name, age):
		Person.__init__(self, age)
		self.age = age 

	def __repr__(self):
		return f"{self.first_name}, {self.last_name}, {self.age}"