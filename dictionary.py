#ESTRUCTURAS DE DATOS: "DICCIONARIOS"
#SINTÁXIS______________________________________
classmates = {
    'Juan' : [12,True],
    'Cristina': 11,
    'Thomas': 13
}

#se puede iterar en los diccionarios
#ya sea por los valores o por las keys

for keys in classmates.keys():
    print(keys)

##-----------------------------------

for values in classmates.values():
    print(values)

#------------------------------------

for keys,values in classmates.items():
    print(keys,values) #nos da la llave y el valor de esta