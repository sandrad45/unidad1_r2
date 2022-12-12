'''
Nombre: Sandra Dania Gonzalez Manzano 
Fecha:  04 / Oct /2022
Descripción: 
    Proyectar y escribir funciones con parámetros.
    Utilizar la sentencia return.
    Construir un conjunto de funciones de utilidad.
    Utilizar las funciones propias del estudiante.
'''
def is_prime(num):
#
# Escribe tu código aquí.
#
 div = 2
 while div < num: 
     if num % div == 0: 
       return False
     div = div + 1
 return True 

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()