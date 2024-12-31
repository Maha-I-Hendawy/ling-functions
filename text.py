class Text:
	def __init__(self, text):
		self.text = text 

	
	def words(self):
		return self.text.split()


	def sents(self):
		return self.text.split('.')



