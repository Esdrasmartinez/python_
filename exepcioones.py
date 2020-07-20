#TRY AND EXCEPT

def dividir_lista(lista,divisor):
    try: 
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(f'El error es {e}')
        return lista


lista = list(range(15))
divisor = int(input('Escoge un número: '))
print(dividir_lista(lista,divisor))

#si es imposible hacer la division nos arroja el error
#solo si es 0