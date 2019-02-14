#######    Definicion de la clase Nodo    #########

class Nodo:
	numero = 0
	hijos = []
	descripcion = ""
	esMeta = False 

	def __init__(self, num_estado, hijos, descripcion, esMeta):
		self.numero = int(num_estado)
		self.hijos = [int(x) for x in hijos]
		self.descripcion = descripcion
		if esMeta == 'si': self.esMeta = True

	def conseguirHijos(self):
		return self.hijos

	def conseguirEsMeta(self):
		return self.esMeta

	def conseguirDescripcion(self):
		return self.descripcion

	def conseguirNumero(self):
		return self.numero
