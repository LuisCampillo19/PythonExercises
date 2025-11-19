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

def numberListAverage():
    numbers = []
    while True:
        num = input("Ingresa un número (o 'fin' para terminar): ")
        if num.lower() == 'fin':
            break
        try:
            numbers.append(float(num))
        except ValueError:
            print("Ingresa un número")
    
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"El promedio de los números ingresados es: {average}\n")
    else:
        print("No hay número ingresados\n")

def evenNumbers():
    numbers = []
    while True:
        num = input("Ingresa un número (o 'fin' para terminar): ")
        if num.lower() == 'fin':
            break
        try:
            number = int(num)
            if number % 2 == 0:
                numbers.append(number)
        except ValueError:
            print("Ingresa un número válido")
    
    print(f"Números pares ingresados: {numbers}\n")

def removeDuplicates():
    numbers = []
    while True:
        num = input("Ingresa un número (o 'fin' para terminar): ")
        if num.lower() == 'fin':
            break
        try:
            number = int(num)
            if number not in numbers:
                numbers.append(number)
        except ValueError:
            print("Ingresa un número válido")
    
    print(f"Números sin duplicados: {numbers}\n")

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
        numberListAverage()
    elif option == "5":
        evenNumbers()
    elif option == "6":
        removeDuplicates()
    elif option == "7":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.\n")