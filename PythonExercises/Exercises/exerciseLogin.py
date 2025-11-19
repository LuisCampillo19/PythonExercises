correctPassword = "Asd.123*"
attemps = 0
maxAttemps = 3

while attemps < maxAttemps:
    userPassword = input("Digite la contraseña del usuario de la corte 6 de los PC de Riwi: ")

    if userPassword != correctPassword:
        attemps += 1
        remainingAttemps = maxAttemps - attemps
        if remainingAttemps > 0:
            print(f"Contraseña intecorrecta. te quedan {remainingAttemps} intentos")
        else:
            print("Ya no tienes más intentos")
    else:
        print("contraseña correcta my brother")
        print("bienvenido mi loco")
        break
