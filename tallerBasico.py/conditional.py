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

def evenOrOddNumber():
    number = int(input("¿Qué número quieres validar? "))

    if number % 2 == 0:
        print(f"el número {number} es par\n\n")
    else:
        print(f"el número {number} es impar\n\n")

def basicCalculator():

    while True:
        print("------ Calculadora Básica --------")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Volver al menú principal")

        opt = input("Ingresa una opción: ")

        if opt == "1":
            a = int(input("Ingresa un número: "))
            b = int(input("Ingresa un número: "))

            c = a + b
            print(f"la suma de {a} + {b} = {c}\n\n")
        elif opt == "2":
            a = int(input("Ingresa un número: "))
            b = int(input("Ingresa un número: "))

            c = a - b
            print(f"la resta de {a} - {b} = {c}\n\n")            
        elif opt == "3":
            a = int(input("Ingresa un número: "))
            b = int(input("Ingresa un número: "))

            c = a * b
            print(f"la multiplicación de {a} x {b} = {c}\n\n")   
        elif opt == "4":
            a = int(input("Ingresa un número: "))
            b = int(input("Ingresa un número: "))

            if b != 0:
                c = a / b
                print(f"la división de {a} / {b} = {c}\n\n")
            else:
                print("No se puede dividir entre 0")
        elif opt == "5":
            print("Saliendo de la calculadora básica...\n\n")
            break
        else:
            print("Opción invalida. Intenta de nuevo\n")

def gradeNotes():
    n = float(input("¿Qué nota sacaste en el examen? "))
    
    if n <= 5.0 and n >4.0:
        print("Excelente\n\n")
    elif n <= 3.9 and n >= 3.0:
        print("Aprobado\n\n")
    elif n >0 and n <= 2.9:
        print("Reprobado\n\n")
    else:
        print("Esta fuera del rango\n\n")

def compareNumbers():
    
    number1 = int(input("Dame el primer dígito a comparar: "))
    number2 = int(input("Dame el segundo dígito a comparar: "))
    number3 = int(input("Dame el tercer dígito a comparar: "))

    maxNumber = number1
    minNumber = number1

    if number2 > maxNumber:
        maxNumber = number2
    if number3 >maxNumber:
        maxNumber = number3
    
    if number2 < minNumber:
        minNumber = number2
    if number3 < minNumber:
        minNumber = number3
    print(f"El número mayor es {maxNumber} y el númer más pequeño de los tres es {minNumber}\n\n")

while True:
    showMenuCo()
        
    option = input("Ingresa una opción del 1 al 7: ")

    if option == "1":
        legalAge()
    elif option == "2":
        numberPoNe()
    elif option == "3":
        evenOrOddNumber()
    elif option == "4":
        basicCalculator()
    elif option == "5":
        gradeNotes()
    elif option == "6":
        compareNumbers()
    elif option == "7":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intenta de nuevo")
