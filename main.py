from persona import Personas
from cliente import Cliente
from cajero import Cajero

fer = Cliente(77322232,5000,"fernando","diaz",23399899,"Juan larrea 1859",24)
pedro = Cliente(87924232,15000,"pedro","gonzalez",17399899,"velez sarfiels 859",54)

listaclientes=[fer,pedro]
listacliente.proximocliente()

fer.consultar()
fer.datos_cliente()

fer.extraer(2000)
fer.datos_cliente()

fer.depositar(100)
fer.datos_cliente()


