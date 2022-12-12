
'''
Nombre: Sandra Dania Gonzalez Manzano
Fecha:  26 / sep /2022
Descripción: Es un programa donde se calcula la altura de una piramide hecha con un numero de bloques. 
'''
blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#	
height=0
while blocks > height: 
    height = height + 1
    blocks = blocks - height

print("La altura de la pirámide:", height)