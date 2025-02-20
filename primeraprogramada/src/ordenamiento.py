class Ordenamiento:
    @staticmethod
    def ordenamiento_burbuja(lista, comparador=None, count=False):
        n = len(lista)
        comparaciones = 0
        intercambios = 0

        for i in range(n - 1):
            for j in range(n - 1 - i):
                comparaciones += 1
                if comparador:
                    resultado = comparador.comparar(lista[j], lista[j + 1])
                    condicion = resultado == 1
                else:
                    condicion = lista[j] < lista[j + 1]

                if condicion:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    intercambios += 1
        return (comparaciones, intercambios) if count else None

    @staticmethod
    def ordenamiento_por_insercion(lista, comparador=None, count=False):
        comparaciones = 0
        intercambios = 0
        for i in range(1, len(lista)):
            clave = lista[i]
            j = i - 1
            while j >= 0:
                comparaciones += 1
                if comparador:
                    resultado = comparador.comparar(clave, lista[j])
                    condicion = resultado == 1
                else:
                    condicion = clave > lista[j]

                if condicion:
                    lista[j + 1] = lista[j]
                    intercambios += 1
                    j -= 1
                else:
                    break
            lista[j + 1] = clave
        return (comparaciones, intercambios) if count else None

    @staticmethod
    def ordenamiento_por_mezcla(lista, comparador=None, count=False):
        def mezclar(izquierda, derecha):
            mezclado = []
            i = j = 0
            comparaciones = 0
            intercambios = 0

            while i < len(izquierda) and j < len(derecha):
                if comparador:
                    resultado = comparador.comparar(izquierda[i], derecha[j])
                    condicion = resultado == 1
                else:
                    condicion = izquierda[i] > derecha[j]

                comparaciones += 1
                if condicion:
                    mezclado.append(izquierda[i])
                    i += 1
                else:
                    mezclado.append(derecha[j])
                    j += 1
                intercambios += 1

            mezclado += izquierda[i:]
            mezclado += derecha[j:]
            return mezclado, comparaciones, intercambios

        if len(lista) <= 1:
            return (lista, 0, 0) if count else (lista, 0, 0)

        medio = len(lista) // 2
        izquierda, comp_izq, inter_izq = Ordenamiento.ordenamiento_por_mezcla(lista[:medio], comparador, count)
        derecha, comp_der, inter_der = Ordenamiento.ordenamiento_por_mezcla(lista[medio:], comparador, count)

        mezclado, comp_mezcla, inter_mezcla = mezclar(izquierda, derecha)
        total_comparaciones = comp_izq + comp_der + comp_mezcla
        total_intercambios = inter_izq + inter_der + inter_mezcla

        return (mezclado, total_comparaciones, total_intercambios) if count else (mezclado, 0, 0)

    @staticmethod
    def ordenamiento_rapido(lista, comparador=None, count=False):
        def _particionar(bajo, alto):
            pivote = lista[alto]
            i = bajo - 1
            comparaciones = 0
            intercambios = 0

            for j in range(bajo, alto):
                comparaciones += 1
                if comparador:
                    resultado = comparador.comparar(lista[j], pivote)
                    condicion = resultado == 1
                else:
                    condicion = lista[j] > pivote

                if condicion:
                    i += 1
                    lista[i], lista[j] = lista[j], lista[i]
                    intercambios += 1

            lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
            intercambios += 1
            return i + 1, comparaciones, intercambios

        pila = []
        total_comparaciones = 0
        total_intercambios = 0

        pila.append((0, len(lista) - 1))

        while pila:
            bajo, alto = pila.pop()
            if bajo < alto:
                indice_pivote, comp_part, inter_part = _particionar(bajo, alto)
                total_comparaciones += comp_part
                total_intercambios += inter_part

                if indice_pivote - bajo < alto - indice_pivote:
                    pila.append((indice_pivote + 1, alto))
                    pila.append((bajo, indice_pivote - 1))
                else:
                    pila.append((bajo, indice_pivote - 1))
                    pila.append((indice_pivote + 1, alto))

        return (total_comparaciones, total_intercambios) if count else None