import random
import time



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
        main_iter = 0w ad  q 

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
        
        print(f'Medio --> Posicion: {medio} / Valor: {lista[medio]}')
        print('-----------------------------------------------------------')
        print(izquierda, '__________', derecha)
        
        print(lista)
        

if __name__ == "__main__":
    list_lenght = int(input('Escoge la longitud de elementos de tu lista: '))
    #lista = [random.randint(0,100) for i in range(list_lenght)]
    lista = [1,9,6,3,9,4,7,2]
    print(f'Lista a ordenar: {lista}')
    start = time.time()
    mix_sort(lista)
    end = time.time()
    duration = end - start
   
    print(f'Lista ordenada en {duration}´s')

