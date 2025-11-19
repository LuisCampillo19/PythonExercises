fruits = ["pears", "strawberries", "apples"]

for index, fruits in enumerate(fruits):
    print(f"{index}:{fruits}")

# si quiero que empiece desde 1, puedo darle la condición
print("Empezar con 1")
fruits = ["pears", "strawberries", "apples"]

for index, fruits in enumerate(fruits, start=1):
    print(f"{index}:{fruits}")

# Usando len()
print("También podemos decirle que nos de cuantos elementos existen dentro de la lista")

fruits = ["pears", "strawberries", "apples"]

for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# ahora lo haremos con tuplas
print("las tuplas son lo mismo")

cities = ("Medellin","Bogota","Cali")

for city in cities:
    print(city)

# Carateres
print("El espacio en blanco también es un carácter, entonces por ende, saldrá")

message = "Hola Riwi"

for i in message:
    print(i)

#Interrucción con BREAK
print("Utilizaremos la palabra reservada BREAK para detener el programa cuando encuentre el número más grande")

numbers = [1, 3, 4, 5, 15, 22, 18, 1]
max = 10

for number in numbers:
    if number > max:
        print(f"el número mayor a {max} es: {number}")
        break # Definimos break para terminar el ciclo con el primero número mayor que encuentre
else:
    print(f"No se a encontrado ningún número mayor a {max}")


#Interrucción con CONTINUE
print("Utilizaremos la palabra reservada CONTINUE para continuar con el siguiente")

numbersContinue = [1,2,3,4,5,6,7,8,9,10]

for numb in numbersContinue:
    if numb %2!=0: #si es true sale del ciclo, al siguiente, sin imprimir, repoite. Si es verdadero "continua" e imprime
        continue
    print(f"Número: {numb}")



