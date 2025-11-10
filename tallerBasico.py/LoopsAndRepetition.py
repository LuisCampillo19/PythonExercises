import random

def showMenuLoops():
    print("-------------------- MENÚ PRINCIPAL -----------------------")
    print("1. Contar del 1 al 10")
    print("2. Sumatoria del 1 al n")
    print("3. Tabla de multiplicar")
    print("4. Contador regresivo con while")
    print("5. Número random de 1 a 100")
    print("6. sumar hasta que el usuario escriba 0")
    print("7. Salir")

def counter():
    count = 0

    while count < 10:
        count +=1
        print(f"{count}\n")

def countdownTimer():
    n = int(input("¿Desde dónde quieres empezar la cuenta recresiva? ")) #5
    count = n
            
    while count >= 0:
        print(f"{count}\n")
        count -=1 

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

def rndm():
    numb = random.randint(1,100)
    print(f"El número random de 1 a 100 fue {numb}\n\n")

def sumZero():
    suma = 0
    while True:
        n = int(input("Suma un número (si el número es 0 todo termina): "))

        if n == 0: 
            print(f"La suma total es {suma}\n\n")
            break
        suma += n 

while True:
    showMenuLoops()
        
    option = input("Ingresa una opción del 1 al 7: ")

    if option == "1":
        counter()
    elif option == "2":
        addtion()
    elif option == "3":
        multiplicationTable()
    elif option == "4":
        countdownTimer()
    elif option == "5":
        rndm()
    elif option == "6":
        sumZero()
    elif option == "7":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intenta de nuevo")