# ['__annotations__', '__builtins__', '__cached__', 
# '__doc__', '__file__', '__loader__', 
# '__name__', '__package__', '__spec__']
print(dir())

#dir(name) enumerated the directorys from name
print(dir(__builtins__))


""" pow(base, exp, mod=None)
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments

    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

None """
print(help(pow))

print(pow(2,3))

# The modules are folders that contains other Python 
# objects. You can see the list of available modules, 
# call help("modules")

print(help('modules'))

import math 

#Show methods from math
print(dir(math))

# radians(x, /)
    # Convert angle x from degrees to radians.
print(help(math.radians))

# 3.141592653589793
print(math.radians(180))