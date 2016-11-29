class Personas():
	def __init__(self,nombre,apellido,dni,direccion,edad):
		self.nombre=nombre
		self.apellido=apellido
		self.dni=dni
		self.direccion=direccion
		self.edad=edad

	def setnombre(self,nombre):
		self.nombre=nombre

	def getnombre(self):
		return self.nombre


	def setapellido(self,apellido):
		self.apellido=apellido

	def getapellido(self):
		return self.apellido


	def setdni(self,dni):
		self.dni=dni

	def getdni(self):
		return self.dni


	def setdireccion(self,direccion):
		self.direccion=direccion

	def getdireccion(self):
		return self.direccion


	def setedad(self,edad):
		self.edad=edad

	def getedad(self):
		 return self.edad

	def datos_personas(self):
		print("los datos de la persona es:",self.nombre,self.apellido,self.dni,self.direccion,self.edad)




