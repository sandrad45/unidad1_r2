'''
Nombre: Sandra Dania Gonzalez Manzano 
Fecha:  04 / Oct /2022
Descripción: 
Define funciones que lee valor de usuario 
y regresa valor leido 
'''
import math


def formula(a,b,c): 
    for1 = (b + math.sqrt( ((b*b) - (4*a*c)))) / (2 * a)
    for2 =  (b - math.sqrt( ((b*b) - (4*a*c)))) / (2 * a)
    print(for1)
    print(for2)
print(formula(6,19,7))
