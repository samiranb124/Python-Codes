"""

a=9
b=4
c=sum((a,b))  # in SUM function there must be present a tuple or a list
print(c)         """

# Function
"""
def function1():
    print("Hello")
function1()    


def function2(a,b):
    print(a+b)
function2(2,3)        



def function1(a,b):
    avg=(a+b)/2
    return avg    # if we not print only RETURN Value then in function call the function is to store in a variable
v= function1(2,4)
print(v)    

"""



# doc string

def function1(a,b):
    """ This return only average value of two numbers      
    this is not working for three  numbers""" #doc string used for knowing what this program do
    avg=(a+b)/2
    return avg
print(function1.__doc__)  # by this the abeove comment is print
v=function1(2,4)
print(v)

