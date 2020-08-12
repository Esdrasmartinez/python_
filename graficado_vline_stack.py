from bokeh.models import ColumnDataSource
from bokeh.plotting import figure,output_file,show

#x_values = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1,
# 2, 3,4,5 6, 7, 8, 9, 10, 13, 14, 15, 16, 17]

output_file = 'spain_vs_mexico_line.html'
#_______________________________________________________________________________________________
x_values = list(range(34))


#________________________________________________________________________________________________

source = ColumnDataSource(data = dict(
    x_values = list(range(34)),

    spain_y_values = [323,181,219,355,585,307,363,334,232,248,334,400,419,564,301,200,301
    ,388,444,442,709,976,1244,341,383,543,852,1249,1646,2045,666,875,1361,1400],
    
    mexico_y_values = [4147,3427,4599,4930,5662,5030,4717,5343,4577,6288,5437,6104,5441,4410,4050,
    3805,5432,5681,6741,6740,6914,4683,4902,6258,6995,7280,6891,6094,4482,4685,7051,6149,6406,7257]
))

p = figure()
#p.vline_stack(['spain_y_values','mexico_y_values'], x = 'x_values', source = source, line_width = 2, color = 'firebrick') 
#p.varea_stack(['spain_y_values','mexico_y_values'], x = 'x_values',color = ["aqua" , "blueviolet"],source = source)
p.hbar_stack(['spain_y_values','mexico_y_values'], y = 'x_values',height = 0.8 ,color = ["aqua" , "blueviolet"],source = source)
show(p)












