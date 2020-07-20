def apply_functions(num):
    
    operaciones = [abs,float,int]
    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))
    
    return resultado

num = int(input('Escoge un numero: '))
print(apply_functions(num))