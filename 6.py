class Animal():
     def toString(self):
        print("Animal")
        
class Monkey(Animal):
    def toString(self):
        super().toString()
        print("Monkey")
        
a1 = Animal()
a1.toString()

m1 = Monkey()
m1.toString()

# %% Polymor

class Employee():
    
    def raisee(self):
        raiseRate = 0.1
        result = 100 * 100 * raiseRate
        print("Employee: ", result)
        
class ComEng(Employee):
    
    def raisee(self):
        raiseRate = 0.2
        result = 100 * 100 * raiseRate
        print("ComEng: ", result)
        
class ElecEng(Employee):
    
    def raisee(self):
        raiseRate = 0.25
        result = 100 * 100 * raiseRate
        print("ElecEng: ", result)

e1 = Employee()
ce = ComEng()
ee = ElecEng()

employeeList = [ce, ee]

for employee in employeeList:
    employee.raisee()
































