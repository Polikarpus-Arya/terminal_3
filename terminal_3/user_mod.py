import os

class User:
	
	# This class handle every single information
	# for each user
	
	def __init__(self, uName, *args):
		if len(args) == 0:
			self.path     = os.getcwd()
			data = open('database/user/' + uName)
			data = list(map(str, data.read().split('\n')))
			self.uName    = data[0]
			self.password = data[1]
		else:
			self.uName    = uName
			self.password = args[0]

			data = ''
			data = data + self.uName + '\n'
			data = data + self.password

			file = open('database/user/' + self.uName, 'w')
			file.write(data)

	def save(self):
		data = ''
		data = data + self.uName + '\n'
		data = data + self.password
		file = open('database/user/' + self.uName, 'w')
		file.write(data)

	# Username
	def setUName(self, uName):
		os.rename('database/user/' + self.uName, 'database/user/' + uName)
		self.uName = uName

	def getUName(self):
		return self.uName

	# Password
	def setPassword(self, password):
		self.password = password

	def getPassword(self):
		return self.password

	# check username and password
	def checkPass(self, uName, password):
		return self.uName == uName and self.password == password