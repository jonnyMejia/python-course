cadena="Hola mundo"

print(cadena[:])
print(cadena[:4])
print(cadena[5:])
print(cadena[1])
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
x=cadena2.split(',')
for e in x :
    print(e)

print("*****************")
#Imprimir Variables de texto
Nombre="Jonny "
Apellido="Mejia"

print(Nombre+Apellido)

print("*****************")
#.Format
    #Orden
Hola="Hola"
Mundo="Mundo"
print("{1} {0}".format(Hola,Mundo))
    #Value Conversion
class Data(object):
    def __str__(self):
        return "str"
    def __repr__(self):
        return "repr"    
    

#metodo __repr__ define el nombre del objeto enASCI
#metodo __str__ es como el tostring del object

print("{0!r}  {0!s}".format(Data(),Data()))