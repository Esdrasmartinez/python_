from bokeh.plotting import figure, output_file, show
 
if __name__ == "__main__":
    output_file(Graficado_simple.html)
    fig = figure()
    total_values = int(input('Cuantos valores deseas graficar: '))

    x_vals = list(range(total_values))

    y_vals = [] 

    for x in x_vals:
        val = int(input(f'Escoge el valor de y para la posición {x} de las abscisas: '))
        y_vals.append(val)

    fig.line(x_vals,y_vals, line_width = 2)
    show(fig)
    print('hello world')
    