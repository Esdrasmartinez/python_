import random
list_nums = sorted([random.randint(0,100) for i in range(100)])
objetivo = int(input('Que numero quieres encontrar: '))


def lineal_search(lista,objetivo,_iter = 1):
    encontrado = None
    for num  in lista:
        _iter += 1
        if num == objetivo:
            print('OBJETIVO ENCONTRADO, Numero de iteraciones: ',_iter)
            return True
        else:
            encontrado = False

    if encontrado == False:
        print(f'Objetivo no encontrado, numero de iteraciones {_iter}')
    
lineal_search(list_nums,objetivo)
