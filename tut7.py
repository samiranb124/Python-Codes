#function
"""
def function1(a,b):
    print(a+b)
function1(2,4)      # in this case we can't put more than two value because we only take two variable in function
# so we use argument
"""
# Arguments 
"""
def function2(*args): # argument takes any value of list , or other as a TUPLE
    for item in args:
        print(item)
hrr=["sam","ram","modhu","vinoy","rohit"]  #wwe can put any value in this list
function2(*hrr)
"""
# PRINT SUM BY USE OF ARGUMENT
"""

def function1(*args):
    for item in args:
       print(sum((item)))

hrr=[1,2,3,4,5]
function1(hrr)           """


#keyword Argument
"""
def function1(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} is a {value}")  # use of f string


hrr={"samiran":"good boy","devansh":"body builder","ulka":"sleeping boy"}
function1(**hrr)
"""






