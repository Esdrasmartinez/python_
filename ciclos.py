horas = 1
minutos = 1
segundos = 0
limite = 60
limite_hrs = 24
while segundos <= limite and minutos <= limite and horas <= limite_hrs :
    
    print(f'{horas}:{minutos}:{segundos}')
    segundos += 1

    if segundos == limite:
        segundos = 0
        minutos += 1   
    if minutos == limite:
        minutos = 0
        segundos = 0
        horas += 1
    
   
#O(limite_hrs)
    


 

    
    