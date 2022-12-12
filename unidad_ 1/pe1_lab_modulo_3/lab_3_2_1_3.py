'''
Autor: Gonzalez Manzano Sandra Dania 
Fecha: 27 sep 2022
Descripcion:Operadores de comparación y ejecución condicional
'''
secret_number = 777
print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
number =int (input())

while secret_number !=number:
    print ("!Ja, ja! ¡Estas atrapado en mi bucle!") 
    
    print(
    """
    +==================================+
    | ¡Bienvenido a mi juego, muggle!  |
    | Introduce un número entero       |
    | y adivina qué número he          |
    | elegido para ti.                 |
    | Entonces,                        |
    | ¿Cuál es el número secreto?      |
    +==================================+
    """)
    number =int (input())
    print ("¡Bien hecho, muggle! Eres libre ahora")