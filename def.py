
objetive = int(input('Ingresa un numero: '))
def bin_search(objetivo):

    """  Busqueda binaria de sqrt

    para epsilon = exactitud de answer
    iteracion = dividir el espacio muestral
    returns = sqrt de objetive

    """
    epsilon = 0.001
    low = 0.0
    hight = max(1.0, objetivo)
    answer= (low + objetivo) / 2

    while abs(answer ** 2 - objetivo)  >= epsilon:
        print(abs(answer ** 2 - objetivo))
        print(f'Low = {low} hight: {hight} answer: {answer}' )
        if answer ** 2 < objetivo:
            low = answer 
        else:
            hight = answer
        answer = (hight + low) / 2
    

    return answer

resultado_busqueda_binaria = bin_search(objetive)
print(f'La raiz cuadrada de {objetive} es {resultado_busqueda_binaria}')
help(bin_search)