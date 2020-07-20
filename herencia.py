#La herencia permite jerarquizar las clases desde una 'SUPER CLASE'
#poliformismo permite 
class Paralelogramo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def sacar_altura(self):
        area = self.altura * self.base
        print(f'El area del paralelogramo es: {area}m^2')


rectangulo = Paralelogramo(5,7)
rectangulo.sacar_altura()

class Cuadrado(Paralelogramo):
    def __init__(self,lado):
        super().__init__(lado,lado)

cuadrado =  Cuadrado(5)
cuadrado.sacar_altura()

def main():
    rectangulo = Paralelogramo(5,7)
    rectangulo.sacar_altura()

    cuadrado =  Cuadrado(5)
    cuadrado.sacar_altura()


if __name__ == "__main__":
    main()