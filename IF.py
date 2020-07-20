user_num1 = int(input('Elige un numero a comparar: '))
user_num2 = int(input('Elige un segundo numero a comparar: '))

if user_num1 > user_num2:
    print('El primer numero es mayor que el segundo')
elif user_num1 < user_num2:
    print('El segundo numero es mayor que el primero')
else: 
    print('Los dos numeros son iguales')

    #despues de un if,elif o else se debe saltar una linea y dejar 3 espacios   