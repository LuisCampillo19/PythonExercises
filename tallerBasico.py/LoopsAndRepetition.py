def showMenuLoops():
    print("-------------------- MENÚ PRINCIPAL -----------------------")
    print("1. Contar del 1 al 10")
    print("2. Sumatoria del 1 al n")
    print("3. Tabla de multiplicar")
    print("4. Contador regresivo con while")
    print("5. Adivina el número")
    print("6. sumar hasta que el usuario escriba 0")
    print("7. Salir")

def counter():
    count = 0

    while count < 10:
        count +=1
        print(f"{count}\n")

def addtion():
    n = int(input("¿Hasta dónde quieres sumar? "))
    add = 0
    
    for i in range(1,n + 1):
        add += i
        print(f"La sumatoria de {i} hasta {n} veces es {add}\n")

def multiplicationTable():
    n = int(input("¿Que tabla queres multiplicar? "))

    for i in range(1,11):
        c = i *  n
        print(f"La multiplicación de {i} x {n} = {c}\n")

while True:
    showMenuLoops()
        
    option = input("Ingresa una opción del 1 al 7: ")

    if option == "1":
        counter()
    elif option == "2":
        addtion()
    elif option == "3":
        multiplicationTable()
    # elif option == "4":
    #     basicCalculator()
    # elif option == "5":
    #     gradeNotes()
    # elif option == "6":
    #     compareNumbers()
    # elif option == "7":
    #     print("Saliendo...")
    #     break
    # else:
    #     print("Opción no válida. Intenta de nuevo")