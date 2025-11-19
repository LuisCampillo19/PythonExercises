print(" --------------  INVENTARIO DE PRODUCTOS --------------")

# Solicitar datos de entrada - nombre
name = input("¿Cómo se llama el producto que vas a ingresar? ")

# Ciclo verdadero para mostrar el error en caso tal de equivocarse
while True:
    # Establezco un Try para capturar el error e indicarle al usuario
    try:
        # Doy propiedades definidas a cada variable
        priceInput = float(input(f"¿Qué precio tiene el producto {name}? "))
        qtyInput = int(input(f"¿Cuántos tenemos en el momento de {name}? "))

        # Validamos que sean correctos los campos
        price = float(priceInput)
        qty = int(qtyInput)

        if price <= 0 and qty <= 0:
            print("\nError: Recuerda que deben ser números positivos, tanto la cantidad como el precio")
            continue # Necesitamos volver al ciclo while
        break # si ambas son verdaderas salimos del ciclo

    except ValueError:
        print("\nRecuerda que los datos precio estan establecidos como flotantes y cantidad como enteros. Intenta de nuevo")

# Operación matemática para sacar el costo total
totalCost = price * qty

# Mostramos los resultados esperados
print(" ----------------- REPORTE DEL INVENTARIO --------------------\n")
print(f"Producto: {name} | Precio: {price} | Cantidad: {qty} para un costo total de ${totalCost:.2f}\n")
