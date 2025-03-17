from lista_enlazada_ordenada import lista_doble_enlace
from nodo_doble_enlace import nodo_doble

lista = lista_doble_enlace()
nodo1 = nodo_doble(99)
nodo2 = nodo_doble(21)
nodo3 = nodo_doble("hola")

lista.imprimir()
lista.insertar(nodo1)
print("-----")
lista.insertar(nodo2)
lista.imprimir()
print("++++++")
lista.insertar(nodo3)
lista.imprimir()
print("======")
lista.eliminar(nodo2)
lista.imprimir()