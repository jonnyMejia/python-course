print(dir())

def f():
    pass

# ... '__spec__', 'f']
# Se agrego la funcion f
print(dir())

# <function f at 0x00000158827CBD30>
# Se muestra la direccio de memoria
print(f)

def ping():
    return "ping!"

word_ping=ping()
print(word_ping)

# Someone functions

import math
print(dir(math))

def volume(r):
    """ Returns the volume of a sphere with radius r """
    x= (4.0/3.0)*math.pi*r**3
    print(x)

# 33.510321638291124
volume(2)


def cm(feet = 0 , inches = 0):
    """ Converts a length from feet and inches to centimeters """
    inches_to_cm=inches*2.54
    feet_to_cm=feet*12*2.54
    print(inches_to_cm+feet_to_cm)

# 152.4
cm(feet=5)

# 7.62
cm(inches=3)

# 0.0
cm()

# 160.02
cm(inches=3,feet=5)

# Error en argumentos prederteminados

# SyntaxError: non-default argument follows default argument
""" def g(x= 0,y):
    return x+y """

# Este metodo no genera Error
# Por lo tanto los argumentos prederteminados siempre ponerlos al final
def g(x,y=0):
    return x+y

 