from kruskal import Grafo

# Valores de nodos para Grafo 2 (Grafo Derecho)
valores_nodos_2 = {"a": 1, "b": 2, "c": 3, "d": 4}

# Grafo 2 (Grafo Derecho)
g2 = Grafo(4)

aristas2 = [
    ("a", "b"), ("a", "c"),
    ("b", "c"), ("b", "d"),
    ("c", "d")
]

# Agregar aristas con pesos calculados a partir de los valores de los nodos
for u, v in aristas2:
    g2.agregar_arista(ord(u) - ord('a'), ord(v) - ord('a'), 
                    valores_nodos_2[u] + valores_nodos_2[v])

print("MST para Grafo 2")
g2.kruskal_mst()