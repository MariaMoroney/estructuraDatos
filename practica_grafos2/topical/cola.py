class Cola:
    
    def __init__(self):
        self.__datos = []
        
    def esta_vacia(self):
        return len(self.__datos) == 0
        
    def encolar(self, elemento):
        self.__datos.append(elemento)
        
    def desencolar(self):
        if not self.esta_vacia():
            return self.__datos.pop(0)
        return None