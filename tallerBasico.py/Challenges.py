def showMenuCo():
    print("-------------------- MENÚ PRINCIPAL -----------------------")
    print("1. Sistema de calificaciones")
    print("2. Carrito de compras")
    print("3. Cajero automático")
    print("4. Gestión de estudiantes(mini base de datos)")
    print("5. Calculadora avanzada (usar funciones)")
    print("6. Agenda de contactos (lista de diccionarios)")
    print("7. Salir")

def gradeSystem():
    studentName = input("¿Cómo te llamas? ")
    grades = []
    numGrades = int(input("¿Cuántas notas vas a ingresar? "))

    for i in range(numGrades):
        while True:
            try:
                grade = float(input(f"Ingresa la calificación {i+1} (0-5): "))
                if 0.0 <= grade <= 5.0:
                    grades.append(grade)
                    break
                else:
                    print("Recuerda que debe estar en los rangos (0.0 a 5.0)")
            except ValueError:
                print("Ingresa un número valido por favor")
    
    average = sum(grades) /len(grades)
    highest = max(grades)
    lowest = min(grades)

    if average >= 3.0 and average < 4.0:
        status = "Aprobado"
    elif average >= 4.0 and average <= 5.0:
        status = "Excelente"
    else:
        status ="Reprobado"
    
    print(f"\nReporte de calificaciones para {studentName}:")
    print(f"Calificaciones dadas: {grades}")
    print(f"Promedio: {average:.2f}")
    print(f"Calificación más alta: {highest}")
    print(f"Calificación más baja: {lowest}")
    print(f"Estado: {status}")

def shoppingCart():
    cart = []

    while True:
        print("\nSubmenú Carrito:")
        print("1. Agregar producto")
        print("2. Ver contenido del carrito")
        print("3. Calcular total y Pagar")
        print("4. Volver al menú principal")

        optionCArt = input("Selecciona una opción (1-4): ")
        if optionCArt == "1":
            name = input("Nombre del producto: ")
            try:
                price = float(input("Precio unitario: "))
                qty = int(input("Cantidad: "))
                
                item = {"name":name, "price": price, "quantity": qty}
                cart.append(item)
                print(f"{name} ha sido agregado")
            except ValueError:
                print("Por favor ingresa un número válido para el precio y cantidad.")
        elif optionCArt == "2":
            if not cart:
                print("El carrito está vacío")
            else:
                print("Lista de productos: ")
                for item in cart:
                    subtotal = item['price'] * item['quantity']
                    print(f"{item['name']}: ${item['price']:.2f} x {item['quantity']} = ${subtotal:.2f}")
        elif optionCArt == "3":
            if not cart:
                print("El carrito está vacío, no hay nada que pagar")
            else:
                total = 0
                for item in cart:
                    total += item['price'] * item['quantity']

                print(f"\nTotal a pagar: ${total:.2f}")
                cart.clear()
                print("Gracias por tu compra! El carrito se ha vaciado")
        elif optionCArt == "4":
            break
        else:
            print("No hay opción válida, intenta de nuevo")
    
def atmMachine():
    money = 1000
    
    while True:
        print("\nCajero automático:")
        print("1. Depositar dinero")
        print("2. Ver saldo")
        print("3. Retirar dinero")
        print("4. Volver al menú principal")

        optionATM = input("Selecciona una opción (1-4): ")
        if optionATM == "1":
            try:
                desposit = float(input("¿Cuánto quieres depositar? "))
                if desposit > 0:
                    money += desposit
                    print(f"Ahora tienes ${money:.2f} en tu cuenta")
                else:
                    print("Ingresa una cantidad válida para depositar")
            except ValueError:
                print("Ingresa un número válido por favor")
        elif optionATM == "2":
            print(f"Tu saldo actual es: ${money:.2f}")
        elif optionATM == "3":
            try:
                withdraw = float(input("¿Cuánto quieres retirar? "))
                if withdraw <= 0:
                    print("La cantidad debe ser positiva")
                elif withdraw > money:
                    print(f"Fondos insuficientes. {money:.2f} disponibles")
                else:
                    money -= withdraw
                    print(f"Has retirado ${withdraw:.2f}. Saldo restante: ${money:.2f}")
            except ValueError:
                print("Ingresa un número válido")
        elif optionATM == "4":
            print("Regresando al menú principal")
            break
        else:
            print("Opción no válida, intenta de nuevo")

while True:
    showMenuCo()
        
    option = input("Ingresa una opción del 1 al 7: ")

    if option == "1":
        gradeSystem()
    elif option == "2":
        shoppingCart()
    elif option == "3":
        atmMachine()
    # elif option == "4":
    #     # basicCalculator()
    # elif option == "5":
    #     # gradeNotes()
    # elif option == "6":
    #     # compareNumbers()
    # elif option == "7":
    #     print("Saliendo...")
    #     break
    else:
        print("Opción no válida. Intenta de nuevo")
