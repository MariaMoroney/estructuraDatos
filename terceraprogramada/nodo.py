class Nodo:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        
    def set_next(self, next_node):
        self.__next = next_node
        
    def get_next(self):
        return self.__next
        
    def get_data(self):
        return self.__data
        
    def __str__(self):
        return str(self.__data)