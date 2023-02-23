# use of Decorator 
"""
def function1(func):  # function call inner function 
    def a1():
        print("Executiing now")
        func()
        print("executed")
    return a1
@function1            # decorator    
def function2():
    print("samiran is a good boy")

function2()

"""






# without decorator
"""
def function1(func):  # function call inner function 
    def a1():
        print("Executiing now")
        func()
        print("executed")
    return a1
           
def function2():
    print("samiran is a good boy")

function2=function1(function2)
function2()
"""


# split all character of a string
"""
s="Samiran Biswas"

t=list(filter(lambda i :i in s, s ))
print(t)
p=list(map(str,s))
print(p)
"""



# function collect in a variable
"""
def func():
    print(" subscribe now")
func2=func
del func  # if we delete the main function then we can also called the function value with the help of variable
func2()    """




# oop
"""
class Employee:
    pass
Harry=Employee()
Larry=Employee()

Harry.name="Samiran"
Harry.age="18"
Harry.salary=60000


Larry.name="Moumita"
Larry.age="16"
Larry.salary=80000

print(Larry.name,Harry.name)         """
"""

class Employee:
    no_of_pass=9
    pass
Harry=Employee()
Larry=Employee()

Harry.name="Samiran"
Harry.age="18"
Harry.salary=60000

no_of_pass=8
Larry.name="Moumita"
Larry.age="16"
Larry.salary=80000

#print(Harry.no_of_pass)
#print(Employee.no_of_pass)

print(Larry.__dict__)  # by __dict__ we can see the all variables and it's value in a function


"""




