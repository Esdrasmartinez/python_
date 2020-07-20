#PERMITE MEDDIR LA COMPLEJIDAD ALGORITMICA MIENTRAS ESTE SE ACERCA AL INFINITO
#IMPORTA NADAMAS EL TÉRMINO DE MAYOR PESO O MAYOR X EJEMPLO 2x**2 vale mas que x + 
#NO IMPORTAN VARIACIONES PEQUEÑAS
#BIG O NATATION


#EXISTEN TRES CASOS COMUNES

#_________________________________________CRECIMIENTO LINEAL_____________________________________________________
#EN ESTE CASO EL CRECIMIENTO ES LINEAL Y DEPENDERÁ EXCLUSIVAMENTE DE N
def f(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

#O(n + n) = O(2n) --> O(n)

#_____________________________________CRECIMIENTO POLINOMINIAL________________________________________________________________________
#EN ESTE CASO EL CRECIMIENTO ES EXPONENCIAL Y DEPENDERÁ EXCLUSIVAMENTE DE N * N
  
def x(n):
    for i in range(n):
        print(i)

    for i in range(n * n ):
        print(i)

#________________________________________________________________________________________________________________
def a(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

#SI TENEMOS CICLOS DENTRO DE CICLOS ESTOS SE MULTIPLICAN
#o(n) + O(n * n) --> O(n**2)

#____________________________________________CRECIMIENTO EXPONENCIAL___________________________________________________________________

#CUANTAS VECES SE LLAMADA LA FUNCION SE MULTIPLICARAÁ POR N
def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

#O(2**n) //tiene varias llamadas recursivas y eso hace al algoritmo con un crecimiento recursivo