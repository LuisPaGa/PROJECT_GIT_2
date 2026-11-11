password = 1234
cont = 0
i = 2


while cont < 3:
    user = int(input('Ingrese su contraseña,\npor su seguridad solo tiene 3 intentos: '))
    if user == password:
        print('Bienvenido')
        break
    else:
        print(f'Contraseña inválida, le quedan {i} intentos ')
        cont += 1
        i -= 1    