from nodo_doble_enlace import Nodo_Doble

class Lista_Doble_Ordenada:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insertar(self, persona):
        nuevo_nodo = Nodo_Doble(persona)
        if self.head is None or self.head.get_data().edad > persona.edad:
            nuevo_nodo.set_next(self.head)
            if self.head:
                self.head.set_prev(nuevo_nodo)
            self.head = nuevo_nodo
            if self.tail is None:
                self.tail = nuevo_nodo
            print(f"{persona} fue agregado correctamente.")
            return
            
        current = self.head
        while current.get_next() and current.get_next().get_data().edad < persona.edad:
            current = current.get_next()
            
        nuevo_nodo.set_next(current.get_next())
        nuevo_nodo.set_prev(current)
        if current.get_next():
            current.get_next().set_prev(nuevo_nodo)
        else:
            self.tail = nuevo_nodo
        current.set_next(nuevo_nodo)
        print(f"{persona} fue agregado correctamente.")
        
    def imprimir(self):
        if self.head is None:
            print("La lista está vacía.")
            return
            
        current = self.head
        contador = 0
        while current:
            print(current.get_data())
            current = current.get_next()
            contador += 1
        
        print(f"Total de personas en la lista: {contador}")
        
    def eliminar_por_posicion(self, posicion):
        if self.head is None:
            print("La lista está vacía.")
            return
            
        current = self.head
        index = 0
        while current and index < posicion:
            current = current.get_next()
            index += 1
            
        if current is None:
            print(f"No existe la posición {posicion}. La lista tiene {index} elementos.")
        else:
            if current.get_prev():
                current.get_prev().set_next(current.get_next())
            if current.get_next():
                current.get_next().set_prev(current.get_prev())
            if posicion == 0:
                self.head = current.get_next()
                if self.head:
                    self.head.set_prev(None)
                else:
                    self.tail = None
            print(f"Se eliminó: {current.get_data()}")
            
    def buscar_por_edad(self, edad):
        if self.head is None:
            print("La lista está vacía.")
            return
            
        if abs(self.head.get_data().edad - edad) < abs(self.tail.get_data().edad - edad):
            current = self.head
            direccion = "desde el inicio"
        else:
            current = self.tail
            direccion = "desde el final"
            
        encontrados = []
        while current:
            if current.get_data().edad == edad:
                encontrados.append(current.get_data())
            if direccion == "desde el inicio":
                current = current.get_next()
            else:
                current = current.get_prev()
                
        if encontrados:
            print(f"Personas encontradas con la edad {edad}:")
            for persona in encontrados:
                print(persona)
        else:
            print(f"No se encontró ninguna persona con la edad {edad}.")