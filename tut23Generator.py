# Use of Generator function

def gen(n):
    for i in range(n):
        yield i

g=gen(5)
print(g.__next__())  
print(g.__next__())      


# A string is always a iteratible item