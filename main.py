import nodo, archivos, estructuras
import sys

#######    Problema de la aspiradora    #########
# Por medio de una busqueda DFS, se consigue una
# ruta para que la aspiradora debe seguir

#Clase: Inteligencia Artificial
 

class Main(object):
	"""docstring for Main"""
	def __init__(self, estadoInicial):
		
		self.conseguirRuta(int(estadoInicial))


	def conseguirRuta(self, estadoInicial):
		#Determinacion de los estados
		archivo = archivos.Estados('estados.txt')
		estados = archivo.conseguirEstados()

		#Condiciones iniciales del problema
		nodo_actual = estados[estadoInicial]
		pila = estructuras.Pila()
		ruta_al_nodo = [nodo_actual.conseguirNumero()]
		visitados = []

		#Busqueda DFS (por profundidad)
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