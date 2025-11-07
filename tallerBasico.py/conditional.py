def showMenuCo():
    print("-------------------- MENÚ PRINCIPAL -----------------------")
    print("1. Mayor de edad")
    print("2. Número positivo, negativo o cero")
    print("3. Par o impar")
    print("4. Calculadora básica")
    print("5. Clasificador de notas")
    print("6. Comparador de tres números: mayor y menor")
    print("7. Salir")

def legalAge():
    age = int(input("¿Cuántos años tienes? "))

    if age >17 and age <99:
        print("Eres mayor de edad\n\n")
    else:
        print("Eres menor de edad\n\n")

def numberPoNe():
    number = int(input("¿Qué número quieres validar? "))

    if number <0:
        print(f"el {number} es negativo\n\n")
    elif number >0:
        print(f"el {number} es positivo\n\n")
    else:
        print(f"el {number} es cero\n\n")

while True:
    showMenuCo()
        
    option = input("Ingresa una opción del 1 al 7: ")

    if option == "1":
        legalAge()
    elif option == "2":
        numberPoNe()
    # elif option == "3":
    # elif option == "4":
    # elif option == "5":
    # elif option == "6":
    # elif option == "7":
        print("Saliendo...")
        #break
    # else:
        print("Opción no válida. Intenta de nuevo")
