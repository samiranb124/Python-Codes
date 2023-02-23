def alpha(word):
    first_letter=word[0]
    if first_letter in "aeiou":
        pigword=word+"ay"
    else:
        pigword=word[1:]+first_letter+"ay"
    return pigword

a=alpha("apple")
print(a)


a=alpha("mango")
print(a)

""" PRINT ANSWER

PS D:\Download Customly\Python By Samiran> python -u "d:\Download Customly\Python By Samiran\tut6(thinknext).py"
appleay
angomay """