def showMenuLoops():
    print("-------------------- MENÚ PRINCIPAL -----------------------")
    print("1. Lista de frutas")
    print("2. Agregar y eliminar frutas")
    print("3. Buscar un elemento en la lista")
    print("4. Lista de números y promedio")
    print("5. Números pares: guardar solo los pares")
    print("6. Eliminar duplicados")
    print("7. Salir")

fruit = ["Manzana", "Uva", "Banano", "Naranja", "Sandia", "Pera"]
    
def fruitList():
    print("Lista de frutas:\n")
    for i in fruit:
        print(f"{i}\n")

def addRemoveFruit():
    print("1. Agregar frutas")
    print("2. Eliminar frutas")
    print("3. Volver al menú principal")

    option = input("¿Qué quieres hacer? (recuerda que es de 1 a 3): ")
    if option == "1":
        newFruit = input("¿Qué fruta quieres agregar? ")
        fruit.append(newFruit) #añadir a la lista .append()
        print(f"{newFruit} fue agregada a la lista\n")
    elif option == "2":
        delectFruit = input("¿Qué fruta quieres eliminar? ")
        if delectFruit in fruit:
            fruit.remove(delectFruit)
            print(f"{delectFruit} fue eliminada de la lista\n")
        else:
            print(f"{delectFruit} no se encuentra en la lista\n")
    elif option == "3":
        print("Volviendo al menú principal...\n\n")
    else:
        print("Error de opción. \n\n")

def searchFruit():
    n = input("¿Qué fruta quieres buscar? ")
    if not n:
        print("No ingresaste ninguna fruta.\n")
        return

    matches = [(i + 1, f) for i, f in enumerate(fruit) if n.lower() in f.lower()]
    if matches:
        print("Frutas encontradas:")
        for i, f in matches:
            print(f"{i}. {f}")
        print()
    else:
        print(f"La fruta '{n}' no se encuentra en la lista.\n")
while True:
    showMenuLoops()
    option = input("Selecciona una opción: ")

    if option == "1":
        fruitList()
    elif option == "2":
        addRemoveFruit()
    elif option == "3":
        searchFruit()
    elif option == "4":
        print()
    elif option == "5":
        print()
    elif option == "6":
        print()
    elif option == "7":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.\n")