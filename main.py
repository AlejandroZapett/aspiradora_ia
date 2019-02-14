import nodo, archivos, estructuras
import sys

#######    Problema de la aspiradora    #########
# Por medio de una busqueda DFS, se consigue una
# ruta para que la aspiradora debe seguir

#Clase: Inteligencia Artificial
#Programador: Alejandro Zapett 

class Main(object):
	"""docstring for Main"""
	def __init__(self, estadoInicial):
		"""
		Ejecutar esta seccion de codigo para cuando el programa
		se ejercuta por consola

		print ("El programa acepta un numero del 0 al 8 ")
		estadoInicial = int(input("Ingrese el estado inicial: "))
		if estadoInicial <= 8 and estadoInicial >= 0:
			self.conseguirRuta(estadoInicial)
		else:
			print("Ingresa un numero valido")
		"""
		self.conseguirRuta(int(estadoInicial))


	def conseguirRuta(self, estadoInicial):
		#Determinacion de los estados
		archivo = archivos.Estados('estados.txt')
		estados = archivo.conseguirEstados()

		#Condiciones iniciales del problema
		nodo_actual = estados[estadoInicial]
		#print(str(nodo_inicial.conseguirNumero())+" "+nodo_inicial.conseguirDescripcion())
		pila = estructuras.Pila()
		ruta_al_nodo = [nodo_actual.conseguirNumero()]
		visitados = []

		#Busqueda DFS
		while(nodo_actual.conseguirEsMeta() == False):
			visitados.append(nodo_actual.conseguirNumero())
			for x in nodo_actual.conseguirHijos():
				if x not in visitados:
					pila.push(x)

			nodo_actual = estados[pila.pop()]
			ruta_al_nodo.append(nodo_actual.conseguirNumero())
		ruta_al_nodo.append(nodo_actual.conseguirHijos()[0])

		#resultado de la busqueda
		print(ruta_al_nodo)

if __name__ == '__main__':

	st = sys.argv[1]
	print(st)
	main = Main(st)