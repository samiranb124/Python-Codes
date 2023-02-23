# Try Except Handling

"""
a=2
b="i am a boy"
try:
    print(a+b)
except:
    print("hei a int and string can't added")

    """
"""
def func(x,y):
    try:
        print(x//y)
        print("oo yeah")
    except:
        print("you can't make a result")

func(3,4) 

"""
# try except else    
"""
def func(x,y):
    try:
        c=x//y
    except:
        print("you devidethe number with 0")
    else:   # when there have no any exception then else is executed
        print(c)

func(3,4)     """

# try , except, else, finally
"""
a=3
b="3"
try:
    print(a+b)
except:
    print("you can't add int and string")
finally:   #always executed after try and execept
    print("I LOVE MY INDIA ALWAYS")        
"""

"""
while (1):
    try:
        a=int(input("Enter a integer number"))
        break
    except:
        print("Please enter a integer number")    



"""
