# use of single inheritance

"""

class Employee:
    def __init__(self,aname,asalary,aage,aposition):
        self.name=aname
        self.salary=asalary
        self.age=aage
        self.position=aposition
    def printdetails(self):
        return f"Name of employee is {self.name} salary is {self.salary} and age is {self.age} and whose position is {self.position}"

# Employee is inherited by Programmer

class Programmer(Employee):
    def printprog(self):
        return f"Name of PROGRAMMER Name is {self.name} salary is {self.salary}and age is {self.age} and whose position is {self.position}"

harry=Employee("Samiran","60000","21","Coordinator")
subham=Programmer("Samiran","60000","22","Instrucator")
print(harry.printdetails())  

print(subham.printprog())        """




# Multiple Inheritance
"""
class Employee:
    def __init__(self,aname,asalary,aposition):
        self.name=aname
        self.salary=asalary
        self.position=aposition

    def printdetails(self):
        return f"the name of employee is {self.name} whose salary is {self.salary} and he hold the position {self.position}"    


class Player:
    def __init__(self,agame,arank):
        self.game=agame
        self.rank=arank

    def printgame(self):
        return f"Player wants to play the  {self.game} game and he hold the position in the game is {self.rank}"    


class Coder(Employee,Player):  # we can call the value of Employee , Player also it self also by Coder
    language="c++"
    def printlang(self):
        print(self.language)        


karan=Coder("Samiran","18000","CEO")
p=karan.printdetails()
karan.printlang()
print(p)


"""


#Use of Multilevel Inheritance

class Dad:
    basketball="1"
    def printdetails0(self):
        return f"i can play  basketball in {self.basketball} way" 
class Son(Dad):
    dance="1"
    def printdetails(self):
        return f"i can dance in {self.dance} way" 

class Grandson(Son):
    dance="2"
    def printdetails2(self):
        return f" i can dance in {self.dance} way"

darry=Dad()
larry= Son()
narry=Grandson()

print(narry.printdetails0())