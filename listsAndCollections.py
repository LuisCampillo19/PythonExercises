def showMenuLoops():
    print("-------------------- MENÚ PRINCIPAL -----------------------")
    print("1. Lista de frutas")
    print("2. Agregar y eliminar frutas")
    print("3. Buscar un elemento en la lista")
    print("4. Lista de números y promedio")
    print("5. Números pares: guardar solo los pares")
    print("6. Eliminar duplicados")
    print("7. Salir")

def fruitList():
    fruit = ["Manzana", "Uva", "Banano", "Naranja", "Sandia", "Pera"]
    print("Lista de frutas:\n")
    for i in fruit:
        print(f"{i}\n")

while True:
    showMenuLoops()
    option = input("Selecciona una opción: ")

    if option == "1":
        fruitList()
    elif option == "2":
        print()
    elif option == "3":
        print()
    elif option == "4":
        print()
    elif option == "5":
        print()
    elif option == "6":
        print()
    elif option == "7":
        print("Saliendo...")
        break