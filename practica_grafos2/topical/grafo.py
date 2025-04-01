from queue import Queue

class Grafo:
    def __init__(self):
        self.__matriz = []
        self.__es_dirigido = False
    
    def es_dirigido(self):
        return self.__es_dirigido
    
    def establecer_dirigido(self, dirigido: bool):
        self.__es_dirigido = dirigido
    
    def establecer_matriz(self, matriz):
        self.__matriz = matriz
    
    def establecer_cantidad_nodos(self, cantidad_nodos: int):
        self.__matriz = [[0 for _ in range(cantidad_nodos)] for _ in range(cantidad_nodos)]
    
    def imprimir_matriz(self):
        for fila in self.__matriz:
            print(" ".join(map(str, fila)))
    
    def agregar_arista(self, inicio, fin):
        self.__matriz[inicio][fin] = 1
        if not self.__es_dirigido:
            self.__matriz[fin][inicio] = 1
    
    def listar_nodos_adyacentes(self, nodo):
        lista_adyacentes = self.__matriz[nodo]
        for indice, valor in enumerate(lista_adyacentes):
            if valor == 1:
                print(f"El nodo {nodo} está conectado al nodo {indice}")
    
    def busqueda_en_amplitud(self, inicio):
        cola = Queue()
        procesados = [0] * len(self.__matriz)
        lista_niveles = [len(self.__matriz) + 1000] * len(self.__matriz)
        lista_niveles[inicio] = 0
        procesados[inicio] = 1
        cola.put(inicio)
        while not cola.empty():
            nodo_actual = cola.get()
            lista_adyacentes = self.__matriz[nodo_actual]
            for pos, es_adyacente in enumerate(lista_adyacentes):
                if es_adyacente == 1 and procesados[pos] == 0:
                    procesados[pos] = 1
                    lista_niveles[pos] = lista_niveles[nodo_actual] + 1
                    cola.put(pos)
            procesados[nodo_actual] = 2
        print(lista_niveles)
    
    def busqueda_en_profundidad(self, inicio):
        visitados = set()
        self.__util_bep(inicio, visitados)
    
    def __util_bep(self, nodo, visitados):
        visitados.add(nodo)
        print(f"{nodo}", end=" ")
        for pos, es_adyacente in enumerate(self.__matriz[nodo]):
            if es_adyacente == 1 and pos not in visitados:
                self.__util_bep(pos, visitados)
    
    def ordenamiento_topologico(self):
        visitados = set()
        pila = []
        for i in range(len(self.__matriz)):
            if i not in visitados:
                self.__util_ordenamiento_topo(i, visitados, pila)
        print("Orden Topológico:", pila[::-1])
    
    def __util_ordenamiento_topo(self, nodo, visitados, pila):
        visitados.add(nodo)
        for pos, es_adyacente in enumerate(self.__matriz[nodo]):
            if es_adyacente == 1 and pos not in visitados:
                self.__util_ordenamiento_topo(pos, visitados, pila)
        pila.append(nodo)