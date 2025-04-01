from collections import defaultdict

class Grafo:
    
    def __init__(self, vertices):
        self.v = vertices  # Número de vértices
        self.grafo = []  # Lista para almacenar todas las aristas
    
    # Función para agregar una arista al grafo
    def agregar_arista(self, u, v, w):
        self.grafo.append([u, v, w])
    
    # Función de utilidad para encontrar el conjunto de un elemento i
    # (Utiliza técnica de compresión de ruta)
    def encontrar(self, padre, i):
        if padre[i] == i:
            return i
        return self.encontrar(padre, padre[i])
    
    # Una función que realiza la unión de dos conjuntos x e y
    # (Utiliza unión por rango)
    def unir(self, padre, rango, x, y):
        raiz_x = self.encontrar(padre, x)
        raiz_y = self.encontrar(padre, y)
        
        # Adjuntar árbol de menor rango bajo la raíz del árbol de mayor rango
        if rango[raiz_x] < rango[raiz_y]:
            padre[raiz_x] = raiz_y
        elif rango[raiz_x] > rango[raiz_y]:
            padre[raiz_y] = raiz_x
        else:
            padre[raiz_y] = raiz_x
            rango[raiz_x] += 1
    
    # La función principal para construir el MST utilizando el Algoritmo de Kruskal
    def kruskal_mst(self):
        resultado = []  # Esto almacenará el MST final
        i = 0  # Índice para aristas ordenadas
        e = 0  # Índice para resultado[]
        
        # Paso 1: Ordenar todas las aristas en orden no decreciente de su peso
        self.grafo = sorted(self.grafo, key=lambda item: item[2])
        
        padre = []
        rango = []
        
        # Crear V subconjuntos con elementos individuales
        for nodo in range(self.v):
            padre.append(nodo)
            rango.append(0)
        
        # El número de aristas en MST será V-1
        while e < self.v - 1:
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.encontrar(padre, u)
            y = self.encontrar(padre, v)
            
            # Si incluir esta arista no causa ciclo
            if x != y:
                e = e + 1
                resultado.append([u, v, w])
                self.unir(padre, rango, x, y)
        
        # Imprimir el MST resultante
        costo_minimo = 0
        print("Aristas en el MST construido:")
        for u, v, peso in resultado:
            costo_minimo += peso
            print(f"{u} -- {v} == {peso}")
        print("Costo total del MST:", costo_minimo)