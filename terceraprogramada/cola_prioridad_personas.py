from nodo import Nodo

class Cola_Prioridad_Personas:
    def __init__(self):
        self.head = None
        
    def encolar(self, persona):
        nuevo_nodo = Nodo(persona)
        if self.head is None:
            self.head = nuevo_nodo
            print(f"{persona} fue agregado a la cola.")
            return
            
        if persona.edad >= 65:
            current = self.head
            prev = None
            while current and current.get_data().edad >= 65:
                prev = current
                current = current.get_next()
                
            if prev is None:
                nuevo_nodo.set_next(self.head)
                self.head = nuevo_nodo
            else:
                nuevo_nodo.set_next(prev.get_next())
                prev.set_next(nuevo_nodo)
        else:
            current = self.head
            while current.get_next():
                current = current.get_next()
            current.set_next(nuevo_nodo)
            
        print(f"{persona} fue agregado a la cola con prioridad.")
        
    def desencolar(self):
        if self.head is None:
            print("La cola está vacía. No hay nadie para eliminar.")
            return
            
        persona_eliminada = self.head.get_data()
        self.head = self.head.get_next()
        print(f"Se eliminó: {persona_eliminada}")
        
    def imprimir(self):
        if self.head is None:
            print("La cola está vacía.")
            return
            
        current = self.head
        print("Estado actual de la cola:")
        while current:
            print(current.get_data())
            current = current.get_next()