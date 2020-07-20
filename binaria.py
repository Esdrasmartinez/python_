objetivo = int(input('Ingresa un numero: '))
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
    

print(f'La raiz cuadrada de: {objetivo} es: {answer}')
