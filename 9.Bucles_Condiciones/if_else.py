a=5
b=4

# True
print(a>b)

# 5 es mayor que 4 #IF
if(a>b):
    print(f"{a} es mayor que {b}")

# If and else
""" El valor de c ha sido alterado """
a=6
b=7
c=10 
d=6

if a>c and b>d :
    print(f"{a} es mayor que {c} y {b} es mayor que {d}")
else:
    print(f"La expresion no es correcta si se cambian los valores iniciales")

# Elif and If
edad=18

if edad>18:
    print("Eres mayor de edad")
elif edad==18:
    print("Tienes exactamente 18 años")
else:
    print("Eres menor de edad")