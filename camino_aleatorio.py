from borracho import Borracho_normal
from coordenada import Coordenada 
from campo import Campo

def caminata(campo,borracho,pasos):
    incio  = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
    
    return incio.distancia(campo.obtener_coordenada)

def simular_caminata(pasos,no_de_intentos,tipo_de_borracho):
    borracho = tipo_de_borracho(nombre = 'Esdras')
    origen = Coordenada(0,0)
    distancias = []
    
    for x in range(distancias_de_caminata,borracho):
        campo = Campo()
        campo.anadir_borracho(borracho,origen)
        simulacion_caminata = caminata(campo,borracho,pasos)
        distancias.append(round(simular_caminata,1))

    return distancias

def main(distancias_de_caminata,no_de_intentos,tipo_de_borracho):
    
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos,no_de_intentos,tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias),4)
        distancia_max = max(distancias)
        distancias_min = min(distancias)

        print(f'Borracho:{tipo_de_borracho.__name__} caminata aleatoria:')
        print(f"""
        Media = {distancia_media}
        Max = {distancia_max}
        Min = {distancias_min}
        """)

if __name__ == "__main__":

    distancias_de_caminata = [10,100,1000,10000]
    no_de_intentos = 100

    main(distancias_de_caminata,no_de_intentos,Borracho_normal)