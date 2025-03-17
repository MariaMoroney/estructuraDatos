class Nodo_Doble:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None
        
    def set_next(self, next_node):
        self.__next = next_node
        
    def get_next(self):
        return self.__next
        
    def set_prev(self, prev_node):
        self.__prev = prev_node
        
    def get_prev(self):
        return self.__prev
        
    def get_data(self):
        return self.__data
        
    def __str__(self):
        prev = self.__prev.get_data() if self.__prev else None
        next = self.__next.get_data() if self.__next else None
        return f"Data: {self.__data}, prev = {prev}, next = {next}"