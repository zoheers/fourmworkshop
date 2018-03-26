class Member():
	def __init__(self,name,age):
		self.name=name
		self.age=age


class Post ():
	def __init__(self,title,topic):
		self.title=title
		self.topic=topic

class MemberStore:
	Members=[]
	def add(self,s):
		self.Members.append(s)
	def get_all(self):
		for p in self.Members:
			print p.name , p.age



class PostStore:
	Posts=[]
	def add(self,s):
		self.Posts.append(s)
	def get_all(self):
		for p in self.Posts:
			print p.title +'\n' +p.topic+'\n'
