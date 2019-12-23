num1=-13243453
num2=-13243453
# tienen iguales id 17576480
print(id(num1))
print(id(num2))
# imprime verdadero asi no tengan el mismo id pero valores iguales
print(num1==num2)
# imprime verdadero solo si tienen el mismo id o posicion de memoria
print(num1 is num2)

cad1="hola"
cad2="hola"
# tienen el mismo id 61400608
print(id(cad1))
print(id(cad2))
# imprime verdadero asi no tengan el mismo id
print(cad1==cad2)
# imprime verdadero solo si tienen el mismo id o posicion de memoria
print(cad1 is cad2)

if(cad1 == "hola"):
    print("dijo hola")

# OPERADORES
print(num1<=num2)
print(num1>=num2)
print(num1!=num2)
print(num1<num2)
print(num1>=num2)
