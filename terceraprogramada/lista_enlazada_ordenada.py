from nodo import Nodo

class Lista_Enlazada_Ordenada:
    def __init__(self):
        self.__list = None
        
    def insertar(self, persona):
        nuevo_nodo = Nodo(persona)
        if self.__list is None or self.__list.get_data().edad > persona.edad:
            nuevo_nodo.set_next(self.__list)
            self.__list = nuevo_nodo
            return
            
        current = self.__list
        while current.get_next() is not None and current.get_next().get_data().edad < persona.edad:
            current = current.get_next()
            
        nuevo_nodo.set_next(current.get_next())
        current.set_next(nuevo_nodo)
        
    def imprimir(self):
        current = self.__list
        contador = 0
        while current:
            print(current.get_data())
            current = current.get_next()
            contador += 1
            
        print(f"Total de personas en la lista: {contador}")
        
    def eliminar_por_posicion(self, posicion):
        if self.__list is None:
            print("La lista está vacía.")
            return
            
        if posicion == 0:
            self.__list = self.__list.get_next()
            return
            
        prev = None
        current = self.__list
        index = 0
        while current and index < posicion:
            prev = current
            current = current.get_next()
            index += 1
            
        if current is None:
            print(f"No existe la posición {posicion}. La lista tiene {index} elementos.")
        else:
            prev.set_next(current.get_next())
            print(f"Se eliminó la persona en la posición {posicion}.")