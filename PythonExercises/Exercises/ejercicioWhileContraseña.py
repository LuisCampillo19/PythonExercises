# contraseñaCorrecta = "Python123"
# intentos = 0
# maxIntentos = 3

# while intentos < maxIntentos:
#     contraseñaUsario = input("Ingresa la contraseña: ")
    
#     if contraseñaUsario == contraseñaCorrecta:
#         print("Contraseña correcta")
#         print("Bienvenido al programa")
#         break
#     else:
#         intentos += 1
#         intentosRestantes = maxIntentos - intentos
#         if intentosRestantes > 0:
#             print(f"Contraseña incorrecta. Te quedan  {intentosRestantes} intentos")
#         else:
#             print("Has agotado todos los intentos")

#---------------------------------------------------------------------------------------------------

contraseñaCorrecta = "python123"
contraseñaUsuario = ""

while contraseñaUsuario != contraseñaCorrecta:
    contraseñaUsuario = input("Introduce la contraseña: ")
else:
    print("Contraseña correcta!")

print("bienvenido al programa")