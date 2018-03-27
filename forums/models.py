class Member():

	def __init__(self,name,age):
		self.name=name
		self.age=age

	def __str__(self):
		return 'name : {}\t\tage:{}'.format(self.name,self.age)
 
class Post ():
	def __init__(self,title,topic):
		self.title=title
		self.topic=topic
		
	def __str__(self):
		return 'Title : {}\t\n\nTopic:\n{}\n'.format(self.title , self.topic)


			
            
