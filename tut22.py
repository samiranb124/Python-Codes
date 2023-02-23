"""

class Employee:
    def __init__(self,fname,lname):
        self.name=fname
        self.last=lname
        self.email=f"{self.name}.{self.last}@gmail.com"

   
    def explain(self):
        return f"The emplyee full name is {self.name}{self.last} of class A"

Hum=Employee("Samiran","Biswas")
print(Hum)  
print(Hum.email)      

"""
#property method

"""

class Employee:
    def __init__(self,fname,lname):
        self.name=fname
        self.last=lname
        

    @property
    def email(self):
        return f"{self.name}.{self.last}@gmail.com"

Hum=Employee("Samiran","Biswas")
print(Hum)  
print(Hum.email)   

"""


# string is a iterable item
# int is not a iterable

