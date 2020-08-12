


def suma_nums_pares(n):
    if n == 0:
        return 1
    
    return n + suma_nums_pares(n - 2)



if __name__ == "__main__":
    n = int(input('Elige un número: '))
    if n%2 != 0:
        n -= 1
        
    else: 
        n = n

    resultado = suma_nums_pares(n)
    print(resultado)

    
