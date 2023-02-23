x=10
def printdetails(p):
    global x  # global keyword can change the value of a gobal variable 
    x=30 
    y=30
    print(x+y)
    print(p,"is the programmer")
printdetails("Samiran") 
print(x)   


