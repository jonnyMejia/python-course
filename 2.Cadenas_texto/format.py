from datetime import datetime
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

# output repr str
print("{0!r}  {0!s}".format(Data(),Data()))


#Padding y aligning

# output test******
print("{:<10}".format("test"))

# output test______
print("{:_<10}".format("test"))

# output ******test
print("{:>10}".format("test"))

# output ______test
print("{:_>10}".format("test"))

# output ***test***
print("{:^10}".format("test"))

# output ___test___
print("{:_^10}".format("test"))

#Truncating size Strings

# tamaño 4 output Hola
print("{:.4}".format("Hola Mundo"))

""" format completo posicion 0 del argumento le dare 
formato dentro de un espaciado de 10 alineado a la derecha 
donde la izquierda estara con '_' y con tamaño del 
string 4 desde la posicion 0 del string
 """
#  output ______Hola
print("{0:_>10.4}".format("Hola Mundo"))

#Numbers Padding 

# formatear un numero a string
print("{:d}".format(100))

# formatear un float a un string
print("{:f}".format(100.5))

# output 100.500000
print("{:0>10.2f}".format(100.5))
print("{:0>10d}".format(10))

#Signed numbers 

# agrega el signo con el '+'
# output +100
print("{:+d}".format(100))

# output -100
print("{:+d}".format(-100))

# agrega el signo pero muy a la izquierda dependiendo de cuan espaciado tenga el string
# salida -      100
print("{:=10d}".format(-100))

#Date time 
""" %Para referirme a 
Y->año
m->mes
d->dia
H->hora
M->minutos """
print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))





