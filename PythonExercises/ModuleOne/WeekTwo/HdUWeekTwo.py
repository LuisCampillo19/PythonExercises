# Variable global para utilizar en las funciones
inventory = []

# Método para añadir productos y validar los campos de precio (float) y cantidad (int) con try
def addProduct():
    name = input("¿Cómo se llama el producto? ")
    try:
        price = float(input("¿Que cuesta el producto unitario? "))
        qty = int(input("¿Cuántas unidades existen? "))

        product = {"name": name, "price": price, "quantity": qty}
        inventory.append(product)
        print(f"{name} se ha agregado correctamente")
    except ValueError:
        print("Recuerda ingresar un número válido para el precio(punto decimal) y cantidad(entero)")

# Método para mostrar los productos
def viewProduct():
    # Condición negada para validar si existe algo
    if not inventory:
        print("No hay productos actualmente")
    else: # dado el caso de que exista un producto o un dato dentro de la lista se ejecute
        print("PRODUCTOS: \n")
        for i in inventory: # iteramos en inventario
            subtotal = i['price'] * i['quantity'] # subtotal individual de los productos - precio x cantidad
            print(f"{i['name']}| ${i['price']:.2f} | {i['quantity']} = ${subtotal:.2f}") 

# Método para calcular estadisticas
def calculateStats():
    # otra condición negada para validar
    if not inventory:
        print("No hay productos para calcular datos")
        return # Salida de emergencia para que no se ejecute más código
    
    # declaro variables para almacenar datos, las cantidades en total y el valor en total
    totalInventoryValue = 0
    totalItems = 0

    for i in inventory:
        # itero y sumo cada multiplicación
        totalInventoryValue += i['price'] * i['quantity'] 
        totalItems += i['quantity']

    numUniqueProducts = len(inventory) # Saco el dato de cuantos productos únicos existen dentro de inventario

    print(f"Cantidad de productos distintos: {numUniqueProducts}\n")
    print(f"Total de cantidad en inventario: {totalItems}\n")
    print(f"Valor total del inventario: {totalInventoryValue:.2f}\n")

    # Si la variable contiene más de 0 datos internos
    if numUniqueProducts > 0:
        avgPrice = totalInventoryValue / totalItems # Promedio de valor total dividido la cantidad total de productos
        # dato complejo con función lineal o corta con lambda donde x toma el precio
        # y luego max() o min() indican cual ha sido el valor dado
        maxProduct = max(inventory, key = lambda x: x['price']) 
        minProduct = min(inventory, key = lambda x: x['price'])

        # imprimimos los datos
        print(f"Promedio unitario por cantidad es ${avgPrice:.2f}")
        print(f"El producto más caro es {maxProduct['name']}: {maxProduct['price']:.2f}")
        print(f"El producto más caro es {minProduct['name']}: {minProduct['price']:.2f}")
                         

# un while True para generar un bucle infinito hasta que le digiten el valor del break
# puse el option como cadena por si el usuario ingresa un caracter
# este no se salga, sino que vuelva al menú
while True:
    print("\n 1. Agregar producto\n 2. Mostrar inventario\n 3. Calcular estadisticas\n 4. Salir\n")

    option = input("Qué deseas hacer? (elige del 1 al 4): ")

    if option == "1":
        addProduct()
    elif option == "2":
        viewProduct()
    elif option == "3":
        calculateStats()
    elif option == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Caracter no encontrado. Intenta de nuevo")
