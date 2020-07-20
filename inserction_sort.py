import random
import time
import sys
sys.setrecursionlimit(10 ** 6)
def ordenamiento_por_insercion(lista,_iter = 0,_subiter = 0):

    for indice in range(1, len(lista)):
        _iter += 1
        valor_actual = lista[indice] 
        #print(f'______________________________________________________________')
        #print(f'Valor_actual en la iteracion {_iter} = {valor_actual}')
        posicion_actual = indice
        #print(f'Posicion_actual en la iteracion {_iter} = {posicion_actual}')
        #print(f'______________________________________________________________')
        
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            _subiter += 1
           
            #print(f'iteracion {_iter}, subiteracion {_subiter} = True')
            lista[posicion_actual] = lista[posicion_actual - 1]
            #print(lista[posicion_actual])
            #print(lista[posicion_actual - 1])
            #print(lista)
            posicion_actual -= 1
           
            

        lista[posicion_actual] = valor_actual
        #print(lista)
        _subiter = 0
    print(lista)




def mix_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
      
        #recursive call to each half 
        mix_sort(izquierda)
        mix_sort(derecha)

        #iteradores
        iter_izquierda = 0
        iter_derecha = 0
        main_iter = 0

        #comparaciones
        while iter_izquierda < len(izquierda) and iter_derecha < len(derecha):
            if izquierda[iter_izquierda] < derecha[iter_derecha]:
                lista[main_iter] = izquierda[iter_izquierda]
                iter_izquierda += 1

            else:
                lista[main_iter] = derecha[iter_derecha]
                iter_derecha += 1

            main_iter += 1


        while iter_izquierda < len(izquierda):
            lista[main_iter] = izquierda[iter_izquierda]
            iter_izquierda += 1
            main_iter += 1   

        while iter_derecha < len(derecha):
            lista[main_iter] = derecha[iter_derecha]
            iter_derecha += 1
            main_iter += 1    

    

def mix_sort1(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
      
        #recursive call to each half 
        mix_sort(izquierda)
        mix_sort(derecha)

        #iteradores
        iter_izquierda = 0
        iter_derecha = 0
        main_iter = 0

        #comparaciones
        while iter_izquierda < len(izquierda) and iter_derecha < len(derecha):
            if izquierda[iter_izquierda] < derecha[iter_derecha]:
                lista[main_iter] = izquierda[iter_izquierda]
                iter_izquierda += 1

            else:
                lista[main_iter] = derecha[iter_derecha]
                iter_derecha += 1

            main_iter += 1


        while iter_izquierda < len(izquierda):
            lista[main_iter] = izquierda[iter_izquierda]
            iter_izquierda += 1
            main_iter += 1   

        while iter_derecha < len(derecha):
            lista[main_iter] = derecha[iter_derecha]
            iter_derecha += 1
            main_iter += 1    

    return(lista)
        
  

if __name__ == "__main__":
    user_range = int(input('Escotge la longitud de tu lista: '))
    
    lista = [random.randint(0,10) for i in range(user_range)]
    
    
    start = time.time()
    ordenamiento_por_insercion(lista)
    end = time.time()
    duration = (end - start)
    print(f'Lista ordenada en {duration}s')
    


    print('_________________________________________________________________')


    start1 = time.time()
    mix_sort(lista)
    end1 = time.time()
    duration1 = end1 - start1
    mix_sort1 = mix_sort1(lista)
    print(mix_sort1)
    print(f'Lista ordenada en {duration1}s')


