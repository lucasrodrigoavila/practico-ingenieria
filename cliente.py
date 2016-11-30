from persona import Personas

class Cliente(Personas):
	def __init__(self,numerodecuenta, saldo, nombre,apellido,dni,direccion,edad):
		Personas.__init__(self,nombre,apellido,dni,direccion,edad)
		self.numerodecuenta=numerodecuenta
		self.saldo=saldo

	def consultar(self):
		print("su saldo es ", self.saldo) 

	def depositar(self,saldo):
		self.saldo =self.saldo + saldo
		print("a depositado", saldo, "y su saldo actual es de",self.saldo) 

	def sacardinero(f):
		def nuevafuncion(self,extraer):
			print("iniciando extracion")
			if self.saldo > self.saldo:
				print("no se puede realizar la extracion")
			else:
				print("saldo disponible para una extracion")
				f(self,extraer)
				print("terminando extracion")
		return nuevafuncion
			
	@ sacardinero
	def extraer(self,extraer):
		self.saldo = self.saldo - extraer
		print("su saldo actual es",self.saldo)


	def datos_cliente(self):
		print("los datos del clientes son:",self.nombre, self.apellido,self.dni, self.direccion, self.edad,self.numerodecuenta,self.saldo)



	  
