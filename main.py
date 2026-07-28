import day20_module

day20_module.greet("Ganesh")
result = day20_module.add(10, 20)
print(result)

from day20_module import greet
greet("Ganesh")



from day20_module import greet,add
greet("Ganesh")
print(add(5,7))

from day20_module import *