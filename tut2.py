#mystr="Samiran Is A good Boy"
#print(len(mystr))
#print(mystr[5:])
#print(mystr[::2])
#print(mystr[::-1]) #it reverse the whole line with words
#print(mystr.upper())
#print(mystr.replace("Boy","DJ"))




##List In Python
# list is mutable
"""
grocery=["harpic","bhendi","sam","ulka","pumkin"]
print(grocery)
print(grocery[0])

numbers=[2,4,3,1,5,6,7,8]
print(numbers[2]+numbers[1])
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(len(numbers))
print(max(numbers))
print(min(numbers))
numbers.append(10) # append add a elements in this country
print(numbers)"""


"""
numbers=[2,4,5,3,1,6,7]
numbers.insert(1,34) # 1 is position and 34 is value
print(numbers)
numbers.remove(3)
print(numbers)
numbers.pop() # remove the last number of a list
print(numbers)



numbers=[2,5,43,2,12]
numbers[1]=454 # 1 is position and 454 is the value 
print(numbers)

"""

# Tuple
# Tuple is immutable
"""
tp=(2,1,3,4,5)
print(tp)
tp[1]=34  # we can't change the value of tuple
print(tp)






{}   Dictionary
[]   List
()   Tuple  

"""

# exchange the number of two value
"""
a=1
b=2
a,b=b,a
print(a,b)"""



# Dictionary
"""
d2={"A":"Samiran","B":"Ulka","C":"Devensh","D":"Saket"}
print(d2)
print(d2["A"])
d2["E"]="Rahul"
print(d2)

# for delete any item
del d2["E"]
print(d2)

print(d2.keys())
print(d2.items())
"""
"""
Question -1 
create a Dictionary and take input from the user and return the meaning of the word from the Dictionary


d2={"A":"Samiran","B":"Ulka","C":"Devensh","D":"Saket"}
print("Enter Optaions A/B/C/D and get the meaning of your entered key :")
ww=input()
print(d2[ww])
"""











