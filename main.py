import nodo, archivos, estructuras

#######    Problema de la aspiradora    #########
# Por medio de una búsqueda DFS, se consigue una
# ruta para que la aspiradora debe seguir

#Clase: Inteligencia Artificial
#Programador: Alejandro Zapett 

class Main(object):
	"""docstring for Main"""
	def __init__(self):
		print ("El programa acepta un número del 0 al 8 ")
		estadoInicial = int(input("Ingrese el estado inicial: "))
		if estadoInicial <= 8 and estadoInicial >= 0:
			self.conseguirRuta(estadoInicial)
		else:
			print("Ingresa un número válido")

	def conseguirRuta(self, estadoInicial):
		#Determinación de los estados
		archivo = archivos.Estados('estados.txt')
		estados = archivo.conseguirEstados()

		#Condiciones iniciales del problema
		nodo_actual = estados[estadoInicial]
		#print(str(nodo_inicial.conseguirNumero())+" "+nodo_inicial.conseguirDescripcion())
		pila = estructuras.Pila()
		ruta_al_nodo = [nodo_actual.conseguirNumero()]
		visitados = []

		#Búsqueda DFS
		while(nodo_actual.conseguirEsMeta() == False):
			visitados.append(nodo_actual.conseguirNumero())
			for x in nodo_actual.conseguirHijos():
				if x not in visitados:
					pila.push(x)

			nodo_actual = estados[pila.pop()]
			ruta_al_nodo.append(nodo_actual.conseguirNumero())
		ruta_al_nodo.append(nodo_actual.conseguirHijos()[0])

		#resultado de la búsqueda
		print(ruta_al_nodo)

if __name__ == '__main__':
	main = Main()
	#main.Pruebas()