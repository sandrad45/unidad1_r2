'''
Autor: Gonzalez Manzano Sandra Dania 
Fecha: 27 sep 2022
Descripcion:Operadores de comparación y ejecución condicional
'''

income = float(input ("Introduce el ingreso anual:"))
tax = 0.0
if income < 85528:
    tax = income * 0.18 -556.02
else:
    tax = round
       
tax= round ( tax, 0)
print ("EL impuesto es:", tax, "pesos")