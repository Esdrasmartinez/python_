import time
#AUMENTAR EL LIMITE DE LA RECURSION
import sys  
sys.setrecursionlimit(10000000)
#_________________________________
def factorial_while(n):
    resultado = 1

    while n > 1:
        
        resultado *= n
        n = n - 1
    return resultado   




def factorial_r(n):
    if n == 1:
        return 1
    else:
        return n * factorial_r(n - 1)

if __name__ == "__main__":
    #una forma de medir el tiempo es importanto time y declarando 2 variables
    #start y end la cual será = a time.time() en medio de esas varible ejecutamos la funcion 
    #y despues imprimimos la resta de end - start
    n = 200000
    start = time.time() 
    factorial_while(n)
    end = time.time()
    print(end - start)

    
    start = time.time() 
    factorial_r(n)
    end = time.time()
    print(end - start)