def suma(a, b):
    assert type(a) != int ,TypeError('Mal')
    assert type(b) != int, 'No se permiten floats'
    var = a + b
    return var
a = input('num1 : ')
b = input('num1 : ')

print(suma(a,b))

