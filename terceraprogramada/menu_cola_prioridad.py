from cola_prioridad_personas import Cola_Prioridad_Personas
from persona import Persona

cola = Cola_Prioridad_Personas()

while True:
    print("\nMenú:")
    print("1. Agregar persona a la cola")
    print("2. Listar personas en la cola")
    print("3. Atender (eliminar de la cola)")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        apellido1 = input("Primer apellido: ")
        apellido2 = input("Segundo apellido: ")
        edad = int(input("Edad: "))
        persona = Persona(nombre, apellido1, apellido2, edad)
        cola.encolar(persona)
    elif opcion == "2":
        cola.imprimir()
    elif opcion == "3":
        cola.desencolar()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")