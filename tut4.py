# Loops

"""
list1=["ram","sam","jadu","madhu"]
for item in list1:
    print(item)



intems=["sam",3,2,1,12,32,43,23,45,654,678,3,2,4,6,7,8]
for item in intems:
    if str(item).isnumeric() and item>6:
        print(item)






items=[["harry",4],["larry",7],["merie",45]]
dict1=dict(items)
#print(dict1)
#for item in dict1:
 #   print(item)

for item,numbers in items:
    print(item,numbers)


    """







# while loop
"""
i=0
while(i<45):
    print(i)
    i=i+1
"""
# for loop
"""
for i in range(1,30):
    print(i)    """

# break
"""
i=0
while(1):
    print(i)
    if i==44:
        break
    i=i+1    """

"""

for i in range(100):
    print(i)
    if i==44:
       break    """




while(1):
    var1=int(input("Enter a Integer number : "))
    if var1>100:
        print(" Congrats you have entered greater than 100 ")
        break
    else:
        print("please try again ")
        continue    
