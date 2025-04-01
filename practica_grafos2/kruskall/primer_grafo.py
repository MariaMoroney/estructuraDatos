from kruskal import Grafo

# Valores de nodos para Grafo 1 (Grafo Izquierdo)
valores_nodos_1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}

# Grafo 1 (Grafo Izquierdo)
g1 = Grafo(6)

aristas1 = [
    ("a", "b"), ("a", "f"), ("a", "e"),
    ("b", "c"), ("b", "f"), ("b", "e"),
    ("c", "d"), ("c", "e"),
    ("d", "e"),
    ("e", "f")
]

# Agregar aristas con pesos calculados a partir de los valores de los nodos
for u, v in aristas1:
    g1.agregar_arista(ord(u) - ord('a'), ord(v) - ord('a'),
                   valores_nodos_1[u] + valores_nodos_1[v])

print("MST para Grafo 1")
g1.kruskal_mst()