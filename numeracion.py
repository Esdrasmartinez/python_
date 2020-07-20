user_num = int(input('Escoge un numero entero: '))
limit_test = 0

while limit_test**2 < user_num:
    limit_test += 1
    

if limit_test**2 == user_num:
    print(f'La raiz cuadrada de: {user_num} es: {limit_test}')
    print(f'Cantidad de posibilidades analizadas:    {limit_test}')

else:
    show_options = input('El numero que elegiste no tiene raiz cuadrada exacta \n Deseas visualizar todas las opciones a analizar Y/n')
    

    
    print(show_options)
    if show_options == 'Y' or show_options == 'y':
        objetivo = user_num
        epsilon= 0.01
        pasos = epsilon **2
        respuesta = 0.0 
        iteraciones = 0

        while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
            print(abs(respuesta**2 - objetivo),respuesta)
            respuesta += pasos
            iteraciones += 1

            if abs(respuesta **2 - objetivo) >= epsilon:
               continue

            else:
                print(f'La raiz cuadrada de: {objetivo} es {respuesta} numero de iteraciones: {iteraciones}')


    elif show_options == 'N' or show_options == 'n':
        objetivo = user_num
        epsilon= 0.01
        pasos = epsilon **2
        respuesta = 0.0 
        iteraciones = 0

        while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
            respuesta += pasos
            iteraciones += 1

            if abs(respuesta **2 - objetivo) >= epsilon:
              continue
            else:
                print(f'La raiz cuadrada de: {objetivo} es {respuesta} numero de posibles resultados analizados: {iteraciones}')
        

        

       
        
    else:
         print('ERROR INGRESE UN CARACTER VALIDO')