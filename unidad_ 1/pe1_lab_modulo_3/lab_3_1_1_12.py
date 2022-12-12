'''
Autor: Gonzalez Manzano Sandra Dania 
Fecha: 27 sep 2022
Descripcion:Operadores de comparación y ejecución condicional
'''

year = int(input("Introduce un año:"))

if year %4 != 0: #No es divisible entre 4
    print ('Año común')
elif year % 100 !=0: # Año Bisisesto
    print ('Año Bisiesto')
elif year % 400 != 0:
        print ('Año Común')
else:
    print ("Año Bisiesto")
#
# Escribe tu código aquí.
#	numero %2 == 0: