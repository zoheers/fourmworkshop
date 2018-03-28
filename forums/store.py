class MemberStore:
	Members=[]
	last_id= 1
	def add(self,s):
		s.id=MemberStore.last_id
		MemberStore.Members.append(s)
		MemberStore.last_id += 1
	def get_all(self):
		for p in self.Members:
			print p

	def get_by_id(self,id):
		for x in MemberStore.Members:
			if x.id==id:
				return x
		return "not found"

	def delete(self,id):
		x= self.get_by_id(id)
		if x!="not found":
			MemberStore.Members.remove(x)
			print "member id dele"
		else:
			print  "not exixt"

	def entity_exists(self,id):
		x=self.get_by_id(id)
		if x == "not found":
			return False
		else:
		 return True



class PostStore:
	Posts=[]
	last_id=1
	def add(self,s):
		s.id=PostStore.last_id
		PostStore.Posts.append(s)
		PostStore.last_id+=1

	def get_all(self):
		for p in self.Posts:
			print p

	def get_by_id (self,id):
		for x in PostStore.Posts:
			if x.id==id:
				return x
		return "not found"

	def delete(self,id):
		x= self.get_by_id(id)
		if x!="not found":
			PostStore.Posts.remove(x)
			print "member id dele"
		else:
			print  "not exixt"

	def entity_exists(self,id):
		x=self.get_by_id(id)
		if x == "not found":
			return False
		else:
		 return True
