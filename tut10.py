"""

class Employee:
    def printdef(self):
        return f"the name of employee {self.name} ,salary is {self.salary} and position of the employee is {self.position}"

Harry=Employee()
Larry=Employee()

Harry.name="Samiran"
Harry.position="Teacher"
Harry.salary=60000


Larry.name="Moumita"
Larry.position="HOD"
Larry.salary=80000   

print(Harry.printdef())                """

# Use Of   __init__(self)
"""
class Employee:
    def __init__(self,name,age,salary):
        self.Name=name
        self.Age=age
        self.Salary=salary

    def printdef(self):
        return f"the name of employee is {self.Name} , age and salary is {self.Age}{self.Salary}"    


Harry=Employee("Samiran","18",46000)
print(Harry.Name)
print(Harry.printdef())
"""
# use of class method 

"""

class Employee:
    Increment_5=5  # class variable
    def __init__(self,aname,aage,asalary):
        self.name=aname
        self.age=aage
        self.salary=asalary

    def printdef(self):
        return f"the name of employee is {self.name} whose age is {self.age} and his salary is {self.salary}"    

    
    @classmethod
    def Change_value_increment(cls,newleaves):          # class method
        cls.Increment_5=newleaves

p=Employee("SAMIRAN","21",50000)
p.Change_value_increment(100)
print(p.printdef())
print(p.Increment_5)

"""





