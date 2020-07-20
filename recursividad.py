#n! = n * (n-1)

def factoral(n):
    """ALGORYTH FOR N FACTORIAL

    n= int
    returns n! 
    """ 
    
    print(n)
    if(n == 1):
       
        return 1

   
    return n * factoral(n - 1)
    

n = int(input('Ingresa un numero entero positivo: '))
print(factoral(n))