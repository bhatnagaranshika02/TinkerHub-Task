class Tinkers:
	tinker_count=0
	def __init__(self,name):
		self.stack=[]
		self.title=""
		self.name=name
		self.starttime=None
		self.endtime=None
		Tinkers.tinker_count+=1

	def __del__(self):
		Tinkers.tinker_count-=1

	def addStacks(self,interest):
		self.stack.append(interest)

	def setMentorOrLearner(self,title):
		self.title=title

	def setAvailableTime(self,starttime,endtime):
	#This method sets time in hour in UTC
		if self.title=="Mentor":
			self.starttime=starttime
			self.endtime=endtime

	def getMentor(self,stack,time):
		if stack in self.stack and self.title=="Mentor":
			if time>=self.starttime and time<=self.endtime:
				return True
if __name__=="__main__":
	tinks=[]

	obj1=Tinkers("Rohan")
	obj1.addStacks("Python")
	obj1.setMentorOrLearner("Learner")
	tinks.append(obj1)
	
	obj4=Tinkers("Ronit")
	obj4.addStacks("Java")
	obj4.setMentorOrLearner("Learner")
	tinks.append(obj4)

	obj2=Tinkers("Shyam")
	obj2.addStacks("Python")
	obj2.setMentorOrLearner("Mentor")
	start=12
	end=17
	obj2.setAvailableTime(start,end)
	tinks.append(obj2)

	obj3=Tinkers("Rohit")
	obj3.addStacks("Python")
	obj3.setMentorOrLearner("Mentor")
	start=5
	end=20
	obj3.setAvailableTime(start,end)
	tinks.append(obj3)

	stack="Python"
	time=14
	for obj in tinks:
		if obj.getMentor(stack,time):
			print(obj.name)
		