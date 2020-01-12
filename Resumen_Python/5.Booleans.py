# True is correct
# true is incorrect
print(True)
print(False)

a=3
b=5
print(a==b)
print(a!=b)

# <class 'bool'>
print(type(True))
print(type(False))

print(bool(0))         #False
print(bool(-343))      #True
print(bool(2142.34))   #True

print(bool(" "))        #True
print(bool(''))        #False

print(str(False)+" False") #False False
print(str(True) + " True") #True True

#0 because False=0 and True=1
print(5*False)   #0
print(5+True)    #6