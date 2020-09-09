#from bokeh.plotting import figure, output_file, show
import math
import time

if __name__ == "__main__":
    #output_file('Graficado_simple.html')
    #fig = figure()
    
    print("""
                        ╔════════════════════╗ 
                           BIENVENIDO RATA 
                        ╚════════════════════╝
    """)
    def transposicion(n):
        absolute = abs(n)
        negative = absolute * -1
        positive = absolute * +1

        if n == negative:
            return positive
        if n == positive:
            return negative


    def anadir_signo(n):
        absolute = abs(n)
        negative = absolute * -1
        positive = absolute * +1

        if n == positive:
            positive_sign = str(positive)
            return '+' + positive_sign
        if n == negative:
            return negative
        

    x_vals = []
    y_vals = [] 

    for x in range(2):
        val = float(input(
        f"""                      ══════════════════════════
                        Escoge el valor de X {x+1} 
        """))
        x_vals.append(val)

    for y in range(2):
        val = float(input(
        f"""                      ═══════════════════════════
                        Escoge el valor de Y {y+1}
        """))
        y_vals.append(val)

    cateto1 = abs(x_vals[1]) + abs(x_vals[0])
    cateto2 = abs(y_vals[1])+ abs(y_vals[0])

    hip = math.sqrt(cateto1**2 + cateto2 **2)
    pendiente = (y_vals[1] - y_vals[0]) / (x_vals[1] - x_vals[0]) 
    angulo_inclinacion = math.degrees(math.atan(pendiente))

    #_____________________________________________________________________
    pta1 = pendiente * (-1 * x_vals[0])
    operacion1 = pta1 + transposicion((y_vals[0])*-1)
    #______________________________________________________________________

    ecuación_procedimiento = f"""
                        ╔═══━━━─── • ───━━━═══╗
                        MODELO PUNTO PENDIENTE
                           y - y1 = m*(x-x1)
                        ╚═══━━━─── • ───━━━═══╝

    ---------------------------PROCEDIMIENTO-----------------------------------------
    y - {y_vals[0]} = {pendiente}(x - {x_vals[0]})   
    y - {y_vals[0]} = {pendiente}x  {anadir_signo(pta1)} 
    y - {y_vals[0]}  {anadir_signo(transposicion(pendiente))}x  {anadir_signo(transposicion(pta1))} = 0
    ----------------------------------------------------------------------------------
    """
   
    ecuación_resultado = f"""
    ---------------------------ECUACIONES GENERALES-----------------------------------
                        ┌─────────     ─────────┐
                        y = {anadir_signo(transposicion(y_vals[0]))} {anadir_signo(pendiente)}x  {anadir_signo(pta1)}
                        
                        y = {anadir_signo(pendiente)}x {anadir_signo(operacion1)}
                        └─────────     ─────────┘
    
    """
    
    time.sleep(0.5)

    print(f"""
                ╔╩═══════════════════╩══════════════════╩╗
                    PENDIENTE Y ÁNGULO DE INCLINACIÓN
                ╚╦═══════════════════╦══════════════════╦╝
        {y_vals[1]} - {y_vals[0]}
                --------- = {pendiente}   Ángulo de inclinación = {angulo_inclinacion} 
        {x_vals[1]} - {x_vals[0]}

            Hipotenusa = {hip}u

    
       """)

    ecuacion_opcion = input('DESEAS VER EL PROCEDIMIENTO PARA OBTENER LA ECUACIÓB Y/n')
    if ecuacion_opcion == 'y' or ecuacion_opcion == 'Y':
        print(ecuación_procedimiento)
        time.sleep(0.5)
        print(ecuación_resultado)

    if ecuacion_opcion == 'n' or  ecuacion_opcion == 'N':
        print(ecuación_resultado)


    #y - y1 = m*(x-x1)

    #fig.line(x_vals,y_vals, line_width = 2)
    #show(fig)
    
