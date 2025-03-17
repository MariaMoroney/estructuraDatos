from lista_doble_ordenada import Lista_Doble_Ordenada
from persona import Persona

lista = Lista_Doble_Ordenada()

while True:
    print("\n1. Agregar persona")
    print("2. Listar personas")
    print("3. Borrar persona")
    print("4. Buscar persona por edad")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        apellido1 = input("Primer apellido: ")
        apellido2 = input("Segundo apellido: ")
        edad = int(input("Edad: "))
        persona = Persona(nombre, apellido1, apellido2, edad)
        lista.insertar(persona)
    elif opcion == "2":
        lista.imprimir()
    elif opcion == "3":
        pos = int(input("Ingrese la posición de la persona a borrar: "))
        lista.eliminar_por_posicion(pos)
    elif opcion == "4":
        edad = int(input("Ingrese la edad a buscar: "))
        lista.buscar_por_edad(edad)
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")