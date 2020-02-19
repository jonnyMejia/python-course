# Es una combinacion de clave:valor
colores={"rojo":"red","azul":"blue","verde":"green"}
print(colores)

# imprimir el valor con la clave de la lista->red
print(colores["rojo"])

# Tambien se agregar valores de esta manera
# {'rojo': 'red', 'azul': 'blue', 'verde': 'green', 'negro': 'black'} 
colores["negro"]="black"
print(colores)

# Eliminar un elemento con el metodo "del"
# {'rojo': 'red', 'azul': 'blue', 'verde': 'green'}
del(colores["negro"])
print (colores)

# {'azul': 'blue', 'verde': 'green'}
colores.pop("rojo")
print(colores)

# Recorrer un diccinario
# Imprimir solo las claves
""" azul
verde """
for key in colores:
    print(key)

# Imprimir claves y valores
""" azul blue
verde green """
for key,valor in colores.items():
    print(key,valor)
# se obtiene el indice de posicion junto con su valor
for k,v in enumerate([1,2,3,4]):
    print(k,v)

# Copy() retorna una copia del diccionario actual
dic2=colores.copy()


# el setDefault funciona como get y agregar un nuevo elemento
# Get
print(colores.setdefault("azul"))
# Agregar
colores.setdefault("nuevo","new")
print(colores)
# Limpia todo el diccionario
colores.clear()

""" Metodo update en diccionarios, actualiza el diccionario, si 
se tiene claves repetidas, se utiliza del argumento su valor y se actuliza """

dic1 = {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}
dic2 = {'c' : 6, 'b' : 5, 'e' : 9 , 'f' : 10}
dic1.update(dic2)
print(dic1)
# dic 1 → {'a' : 1, 'b' : 5, 'c' : 6 , 'd' : 4 , 'e' : 9 , 'f' : 10}


# Metodo dict Recibe como parametro una represenatcio de un diccionario 
diccionario=dict(nombre='nestor', apellido='Plasencia', edad=22)
dictionary=dict([("nombre","nestor"),("apellido","plasencia"),("edad",22)])
print(diccionario)
print(dictionary)
# dic → {‘nombre’ : 'nestor', ‘apellido’ : 'Plasencia', ‘edad’ : 22}

# Recibe ZIP dos parametros iterables ya sea una cadena o uan lista o tupla,ambos deben tenr el mismo numero de elementos
# Funiona genial con el metodo dic
dic = dict(zip('abcd',[1,2,3,4]))
print(dic)
# dic →   {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}