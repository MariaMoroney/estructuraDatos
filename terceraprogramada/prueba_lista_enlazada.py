from lista_enlazada_ordenada import Single_Linked_List
from nodo import Nodo

mi_lista = Single_Linked_List()
nodo1 = Nodo(44)
mi_lista.imprimir()
mi_lista.insertar(nodo1)
print("-----")
mi_lista.imprimir()

nodo2 = Nodo(33)
mi_lista.insertar(nodo2)
nodo3 = Nodo(25)
mi_lista.insertar(nodo3)
nodo4 = Nodo(66)
mi_lista.insertar(nodo4)
print("-----")
mi_lista.imprimir()

print("-----++++++++")
mi_lista.eliminar(nodo3)
mi_lista.imprimir()