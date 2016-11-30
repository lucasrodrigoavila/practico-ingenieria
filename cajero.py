from persona import Personas
from cliente import Cliente

class Cajero():
	def __init__(self,codigo_cajero):
		self.codigo_cajero= codigo_cajero
		self.listaclientes= [fer,pedro,ruperto]


	def proximocliente(self):
		try:
			return self.listaclientes.pop(0)
		except:
			raise ValueError("La cola está vacía")

		
	
	

fer = Cliente(77322232,5000,"fernando","diaz",23399899,"Juan larrea 1859",24)
pedro = Cliente(87924232,15000,"pedro","gonzalez",17399899,"velez sarfiels 859",54)
ruperto = Cliente(27432439,500,"ruperto","jerez",23399899,"cabildo 234",24)


	
