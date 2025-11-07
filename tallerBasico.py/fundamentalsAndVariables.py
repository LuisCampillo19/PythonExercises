def showMenuFuVa():
    print("*********** MENÚ PRINCIPAL ****************")
    print("1. Imprimir nombre y edad")
    print("2. Suma de dos números")
    print("3. Sacar el área de un triángulo")
    print("4. Conversor de grados Celsius a Fahrenheit")
    print("5. Saber el tipo de dato de la variable")
    print("6. Edad actual y mostrar cuantos años tendrá en 10 años")
    print("7. Salir")
    
def showNameAge():
    a = input("¿cómo te llamas? ")
    b = input("¿Cuántos años tienes? ")

    print(f"Hola {a}, tienes {b} de edad \n\n")

    return a,b

while True:
    showMenuFuVa()
    option = input("Escoge una opción del 1 al 7: ")

    if option == "1":
            showNameAge()
    elif option == "2":
        print("")
    elif option == "3":
        print("")
    elif option == "4":
        print("")
    elif option == "5":
        print("")
    elif option == "6":
        print("")
    elif option == "7":
        print("GoodBye...")
        break
    else:
        print("Esta opción no existe. Vuelve a intentarlo")


