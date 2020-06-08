# El for se usa para recorrer tantas veces 
# como sea posible e iterar por una lista
colores=["rojo", "verde", "azul"]

for c in colores:
    print(c)

for char in "Hola mundo":
    print(char)

# Range
# [0, 1, 2, 3, 4, 5, 6, 7]
print(list(range(8)))

# [2, 3, 4, 5, 6, 7]
print(list(range(2,8)))

# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list(range(10,0,-1)))
 
""" Funcion RANGE el primer argumento es el valor inicial el 
segundo argumento es el valor final(no cuenta ese numero),
y el tercer numero es de cuanto en cuanto se suma """

# Sentencias break y continue

for i in range(10):
    if i==3:
        continue
    elif i==7:
        print("Romper bucle")
        break
    else:
        print(i)