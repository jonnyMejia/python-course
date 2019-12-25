cadena="Hola mundo"
# imprime Hola mundo
print(cadena[:])
# imprime Hola
print(cadena[:4])
# imprime mundo
print(cadena[5:])
# imprime ola mun-> trasAntepenultimo
print(cadena[1:-2])
# imprime ola mund-> Antepenultimo
print(cadena[1:-1])
# imprime d
print(cadena[-2])

print("*****************")
#Funciones de Cadena

print(cadena.upper())
print(cadena.lower())
print(len(cadena))
print(cadena.split())
print("*****************")
#Funcion SPLIT()
cadena2="Pera,Uva,Pepino,Manzana"
print(cadena2.split(','))
# retorna una lista separando con el ","
x=cadena2.split(',')
# recorremos la lista con el "in" 
for e in x :
    print(e)
print("*****************")
#Imprimir Variables de texto
Nombre="Jonny "
Apellido="Mejia"

print(Nombre+Apellido)

print("*****************")
