
#MAP function  with Lambda function

"""
numbers=["3","4","6","7","9"]
print(numbers)
numbers=list(map(int,numbers))
print(numbers)
"""
"""

def function1(a):
    return a*a
numbers=["3","4","6","7","9"]
p=list(map(int,numbers))
square=list(map(function1,p))
print(square)

"""

"""

def square(a):
    return a*a
def cube(a):
    return a*a*a
func=[square,cube]  #make a list 
for i in range(4):
    val=list(map(lambda x:x(i),func))   # use of lambda function 
    print(val)

"""


#filter function

# use of function
"""
list1=[1,2,3,4,5,6,7,8,9,10,11]
def is_greater_5(num):
    return num>5

greater_5=list(filter(is_greater_5,list1))
print(greater_5)
"""

# use of lambda function
"""
list1=[1,2,3,4,5,6,7,8,9,10,11]
greater_5=list(filter(lambda num:num>5,list1))
print(greater_5)
"""



