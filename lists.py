#XCLONACION DE LISTAS
#Si nosotros creamos una lista y esta se la
#asignamos a una variable habrá un conflicto 
#y ambas variables corresponderán a la lista
list_1 = [1,2,3]
a = list_1
#en este caso list_1 y a corresponden al mismo 
#espacio en memoria para evitar esto usamos
b = list(list_1)
#ahora el contenido de b será igual al de a y 
#list_1 pero corresponderá a otro espacio en  memoria

#---------------------------------------------------------
my_list = list(range(100))
#ASI HACEMOS UNA LISTA CON NÚMEROS DEL 0 AL 99

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#OPERACIONES CON LIST´S
#utilizamos un for loop la variable que va a iterar
#en nuestra lista se modificará x ejemplo  
#fijarse en la sintáxis
double = [ i * 2 for i in my_list]
#de igual forma se pueden poner condiciones x ejemplo

par = [a for a in my_list if a%2 == 0]

#recuerda var_name = [ var for var in list_name condition]

def objetive(a):
    """
    lista.extend(iterable) #extiende la lista con valores dentro de un iterable como un range()
lista.insert(i, ‘valor’) #Agrega un valor en la posición i y recorre todos los demás. No borra nada.
lista.pop(i) #Elimina valor en la posición i de la lista.
lista.remove(‘valor’) #Elimina el primer elemento con ese valor.
lista.clear() #Borra elementos en la lista.
lista.index(‘valor’) #Retorna posición del primer elemento con el valor.
lista.index(‘valor’, start, end) #Retorna posición del elemento con el valor dentro de los elementos desde posición start hasta posición end)
lista.count(‘valor’) #Cuenta cuántas veces esta ese valor en la lista.
lista.sort() #Ordena los elementos de mayor a menor.
lista.sort(reverse = True) #Ordena los elementos de menor a mayor.
lista.reverse() #Invierte los elementos
lista.copy() #Genera una copia de la lista. También útil para clonar listas.

"""
