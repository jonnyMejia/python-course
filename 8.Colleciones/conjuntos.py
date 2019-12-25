# Los conjuntos son immutables, es decir no se puede modificar sus elementos, por lo tanto no puede contener listas, u otros conjuntos, ademas no se pueden indexar
colores={"rojo","azul","verde"}
print(colores)

# Imprimir el tamaño del conjunto
print(len(colores))

# Agregar un elemento 
colores.add("Negro")
print(colores)

# Eliminar un elemento
colores.discard("azul")
print(colores)


