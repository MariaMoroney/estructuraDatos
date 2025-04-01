from grafo import Grafo

def main():
    mi_grafo = Grafo()
    
    # Preguntar si el grafo es dirigido
    es_dirigido = input("¿Es el grafo dirigido? (S/N): ").strip().upper()
    mi_grafo.establecer_dirigido(es_dirigido == "S")
    
    # Configurar número de nodos
    cantidad_nodos = int(input("¿Cuántos nodos tiene el grafo? "))
    mi_grafo.establecer_cantidad_nodos(cantidad_nodos)
    mi_grafo.imprimir_matriz()
    
    # Agregar rutas (aristas)
    agregar_arista = input("¿Desea agregar una arista? (S/N): ").strip().upper()
    while agregar_arista == "S":
        nodo_inicio = int(input("Ingrese nodo de inicio: "))
        nodo_fin = int(input("Ingrese nodo de fin: "))
        mi_grafo.agregar_arista(nodo_inicio, nodo_fin)
        mi_grafo.imprimir_matriz()
        agregar_arista = input("¿Desea agregar otra arista? (S/N): ").strip().upper()
    
    # Mostrar nodos adyacentes
    nodo_a_revisar = int(input("¿De qué nodo desea ver la lista de adyacencia? "))
    mi_grafo.listar_nodos_adyacentes(nodo_a_revisar)
    
    # Ejemplo de ordenamiento topológico
    # mi_grafo.establecer_matriz([
    #     [0, 1, 0, 1, 0, 0],
    #     [0, 0, 0, 0, 1, 0],
    #     [0, 0, 0, 0, 1, 1],
    #     [0, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 1, 0, 0],
    #     [0, 0, 0, 0, 0, 1]
    # ])
    
    print("++++++ Ordenamiento Topológico ++++++")
    mi_grafo.ordenamiento_topologico()
    
    print("********* Búsqueda en Profundidad *********")
    mi_grafo.busqueda_en_profundidad(0)

if __name__ == "__main__":
    main()