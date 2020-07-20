import random 
import time
user_range = int(input('Escoge la longitud de tu lista: '))
objetivo = int(input('Escoger el numero que deseas encontrar'))
_list = sorted([random.randint(0, 100) for i in range(user_range)])


def busqueda_binaria(lista,start,end,objetivo,_iter = 1):
    _iter += 1 
    if start > end:
        return False
    
    medium = (start + end) // 2

    if lista[medium] == objetivo:
        print(f'Numero de recursiones = {_iter}')
        return True 
    elif lista[medium] < objetivo:
        return busqueda_binaria(lista,medium + 1,end,objetivo)

    elif lista[medium] > objetivo:
        return busqueda_binaria(lista,start,medium - 1,objetivo)
    
    else:
        raise ValueError('F')
print(_list)

incicio = time.time()
encontrado = busqueda_binaria(_list,0,len(_list),objetivo)
fin = time.time()
duracion = fin - incicio
print(f'El numero {objetivo} {"Esta" if encontrado else "No esta"} en la lista, Tiempo transcurrido: {duracion}')