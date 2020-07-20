objetivo = int(input('Escoge un número: '))
epsilon= 1
pasos = epsilon **2
respuesta = 0.0 
iteraciones = 0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo))
    respuesta += pasos
    print(respuesta,pasos)
    