#######    Lectura del archivo de estados inicial    #########

import nodo

class Estados:

	archivo = ""
	estados = []

	def __init__(self, archivo):
		self.archivo = archivo
		self.leerEstados()

	def leerEstados(self):
		self.archivo = open(self.archivo, 'r').read()
		for a in self.archivo.split('\n'):
			nodo_a = a.split(":")
			#num de estados, hijos, descripcion, es meta
			estado = nodo.Nodo(nodo_a[0], nodo_a[2].split(','), nodo_a[1], nodo_a[3])
			self.estados.append(estado)
			
	def conseguirEstados(self):
		return self.estados

