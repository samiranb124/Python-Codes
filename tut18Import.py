import tut17Module

print(tut17Module.add(4,3))


from tut17Module import *   # * means access all the internal function of the module
print(multiple(2,4))


from tut17Module import add
print(add(5,4))

