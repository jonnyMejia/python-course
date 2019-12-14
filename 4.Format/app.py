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

print("{0!r}  {0!s}".format(Data(),Data()))


#Padding y aligning

print("{:<10}".format("test"))
print("{:_<10}".format("test"))
print("{:>10}".format("test"))
print("{:_>10}".format("test"))
print("{:^10}".format("test"))
print("{:_^10}".format("test"))

#Truncating size Strings

print("{:.5}".format("Hola Mundo")) 
print("{:>10.5}".format("Hola Mundo"))

#Numbers Padding 

print("{:d}".format(100))
print("{:f}".format(100.5))
print("{:0>10.2f}".format(100.5))
print("{:0>10d}".format(10))

#Signed numbers 

print("{:+d}".format(-100))
print("{: d}".format(-100))
print("{: d}".format(100))
print("{:= 10d}".format(-100))

#Date time 

print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))





