#FILE read and text MODE Use

"""
# Syntex       pointer_name= open("text file name","mode which you want to open the file")

f=open("io.txt","r") # f is a pointer which is point the open function
#content=f.readline()
#content=f.readlines()
#content=f.read()
#print(content)

content=f.read()
for line in content:
    print(line)

f.close()    # we should have to close the open function 

"""

#file write and append mode use


# write
"""
f=open("io2.txt","w")
content=f.write("Samiran Will Go To Delhi")
print(content)
f.close()
"""
#append
"""
f=open("io2.txt","a")
content=f.write("I love you brother")
print(content)
f.close()
"""

# read and write in same time      r+
"""
f=open("io2.txt","r+")
print(f.read())
content=f.write("GOD PLEASE STAY WITH ME ALWAYS")
print(f.read())
f.close()

"""

#tell()     and seek()
"""
f=open("io2.txt")
print(f.readline())
print(f.tell())
f.close()
"""


"""
f=open("io2.txt")
print(f.readline())
f.seek(5)
print(f.readline())
f.close()
"""
"""
answer 


Samiran Will Go To DelhiI love you brotherI love you brother /nI love you brother 

an Will Go To DelhiI love you brotherI love you brother /nI love you brother
"""




