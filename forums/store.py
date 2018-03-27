class MemberStore:
	Members=[]
	def add(self,s):
		self.Members.append(s)
	def get_all(self):
		for p in self.Members:
			print p



class PostStore:
	Posts=[]
	def add(self,s):
		self.Posts.append(s)
	def get_all(self):
		for p in self.Posts:
			print p