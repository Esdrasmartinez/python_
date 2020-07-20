import random

#para crear un numero random se usa la funcion randdom.ranint(rango)


numero_random_entre_1_10 = random.randint(1,10)
print(numero_random_entre_1_10)

#GENERAR UNA LISTA DE NUMEROS RANDOM 
n = int(input('ESCOGE UN LIMITE: '))
list_1 = [random.randint(1,10) for i in range(n)]
print(list_1)