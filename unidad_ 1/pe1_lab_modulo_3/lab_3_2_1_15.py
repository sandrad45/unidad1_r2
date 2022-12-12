
'''
Nombre: González Manzano Sandra Dania 
Fecha:  6 / oct /2022
Descripción: Es un programa donde colocas un numero al azar y no debe ser 0 negativo, sino es 
realiza una serie de operaciones aritmeticas.
'''
c0 = int(input("Ingresa un numero: "))
nume = 0
if c0 < 1: 
    print("El  numero no debe ser 0 o negativo")
while c0 != 1: 
    if c0 % 2 == 0: 
      c0 = c0 / 2
    else: 
     c0= 3 * c0 + 1
    print(c0)
    num = num + 1 
print("Numero de pasos: ", nume)