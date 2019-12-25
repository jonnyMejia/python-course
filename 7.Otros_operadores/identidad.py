# se crea dos listas con contenidos iguales 
fruta1=["Pera","Manzana"]
fruta2=["Pera","Manzana"]
# se crea una tercera lista que apunta a fruta1 son el mismo objeto misma direccion de memoria
fruta3=fruta1
# ambos tienen el mismo id 55639208
print(id(fruta1))
print(id(fruta3))
# valido si son iguales con el is solo si se tratan del mismo objeto
print(fruta3 is fruta1)
# agrego un nuevo valor "naranja"
fruta3.append("Naranja")
# el valor naranja se agrega en ambas listas ['Pera', 'Manzana', 'Naranja']
print(fruta3)
print(fruta1)