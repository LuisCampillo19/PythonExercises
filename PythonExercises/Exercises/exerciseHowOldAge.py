print("Hola, bienvenido! Calculemos la edad actual")

nameUser = input("¿Cómo te llamas? ")
lastNameUser = input("¿Cómo es tu primer apellido? ")
dateOfBirth = int(input("¿En qué año naciste? "))
currentDate = int(input("¿En qué año estamos actualmente? "))

calculationDate = currentDate - dateOfBirth
print(f"Hola, {nameUser} {lastNameUser}. Tu edad en el año {currentDate} es de: {calculationDate}")

