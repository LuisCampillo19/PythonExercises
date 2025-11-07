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

def addNumbers():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo dígito: "))

    c = a + b

    print(f"La suma de los dos números es: {c}\n\n")

def triangularArea():
    a = float(input("Ingresa la base del triangulo: "))
    b = float(input("Ingresa la altura del triangulo: "))

    c = (a * b)/2 #Base por altura divido en dos

    print(f"El área del triangulo es {c}\n\n")

def temperatureCeFa():
    celcius = float(input("Ingresa la temperatura en Celcius (dato numérico): "))
    fahrenheit = (celcius * 9/5) + 32

    print(f"De Celcius a Fahrenheit es: {fahrenheit}\n\n")

def typeData():

    data = input("Ingresa cualquier tipo de dato: ")

    try:
        valueInt = int(data)
        type = "entero (int)"
    except:
        try:
            valueFloat = float(data)
            type = "flotante (float)"
        except:
            type = "cadena (str)"
    
    print(f"El {data} es de tipo {type}")

while True:
    showMenuFuVa()
    option = input("Escoge una opción del 1 al 7: ")

    if option == "1":
        showNameAge()
    elif option == "2":
        addNumbers()
    elif option == "3":
        triangularArea()
    elif option == "4":
        temperatureCeFa()
    elif option == "5":
        typeData()
    elif option == "6":
        print("")
    elif option == "7":
        print("GoodBye...")
        break
    else:
        print("Esta opción no existe. Vuelve a intentarlo\n\n")


