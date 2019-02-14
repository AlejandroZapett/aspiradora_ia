#######    Definicion de pilas y colas    #########

class Pila:
	def __init__(self):
		self.lista = []

	def push(self,elemento):
		self.lista.append(elemento)

	def pop(self):
		return self.lista.pop()

	def esVacio(self):
		return len(self.lista) == 0

class Cola:
	def __init__(self):
		self.lista = []

	def push(self,elemento):
		self.lista.insert(0,elemento)

	def pop(self):
		return self.lista.pop()

	def esVacio(self):
		return len(self.lista) == 0