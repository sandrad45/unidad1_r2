'''
Autor: Gonzalez Manzano Sandra Dania 
Fecha: 27 sep 2022
Descripcion:Operadores de comparación y ejecución condiciona
l'''
# paso 1
Beatles=[]
print("Paso 1:", Beatles)
# paso 2
Beatles.Oppend ("John")
Beatles.Oppend ("Paul")
Beatles.Oppend ("Geoge")
print("Paso 2:", Beatles)
# paso 3
for miembros in range (2):
    Beatles.append (input("Nuevos miemvros de la banda:"))
print("Paso 3:", Beatles)
# paso 4
del Beatles[-1]
del Beatles[-1]
print("Paso 4:", Beatles)
# paso 5
Beatles.insert (0,"Ringo Starr")
print("Paso 5:", Beatles)

# probando la longitud de la lista
print("Los Fav", len(Beatles))
