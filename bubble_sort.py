

def bubble_sort(_list,_iter1 = 0,_iter2 = 0):
    n = len(_list)

    for i in range(n):
        _iter1 += 1
        print(f'Valor de i en la iteracion {_iter1} es: {i}')
        
        for j in range(0,n - i -1 ):
            limit = n - i -1
            
            _iter2 += 1
            print(f'Limite en la subiteracion {_iter2} es {limit}')
            print(f'Valor de j en la iteracion {_iter2} es: {j}')

            if _list[j] > _list[j + 1]:
                _list[j], _list[j + 1] = _list[j + 1] , _list[j]
                print(_list)
            
            elif _list[j] == _list[j + 1]:
                pass
    return _list            



if __name__ == "__main__":
    user_range = int(input('Escoge la longitud de tu lista: '))
    #list_to_order = [random.randint(0,100) for i in range(user_range)]
    list_to_order = [3,7,9,1]
    print(list_to_order)
    

    lista_ordenada = bubble_sort(list_to_order)
    print(lista_ordenada)