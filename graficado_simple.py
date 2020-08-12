from bokeh.plotting import figure, output_file, show
import math
if __name__ == "__main__":
    output_file('Graficado_simple.html')
    fig = figure()
    

    x_vals = []
    y_vals = [] 

    for x in range(2):
        val = int(input(f'Escoge el valor de X {x+1} '))
        x_vals.append(val)

    for y in range(2):
        val = int(input(f'Escoge el valor de Y{y+1}'))
        y_vals.append(val)

    pendiente = (y_vals[1] - y_vals[0]) / (x_vals[0] - x_vals[1]) 
    angulo_inclinacion = math.degrees(math.atan(pendiente))
    
    print(f"""
    {y_vals[1]} - {y_vals[0]}
    --------- = {pendiente}  Ángulo de inclianción = {angulo_inclinacion}
    {x_vals[1]} - {x_vals[0]}
       """)

    

    fig.line(x_vals,y_vals, line_width = 2)
    show(fig)
    
    