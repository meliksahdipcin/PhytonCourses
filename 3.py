class Calc(object):
    
    def __init__(self, a ,b):
        self.value1 = a
        self.value2 = b
        
    def add(self):
        return self.value1 + self.value2
        
    def summ(self):
        return self.value1 - self.value2
        
    def multiply(self):
        return self.value1 * self.value2
        
    def div(self):
        return self.value1 / self.value2
        
print("Choose add(1), sum(2), multiply(3), division(4)")
selection = input("select 1 or 2 or 3 or 4: ")

v1 = int(input("First value: "))
v2 = int(input("Second value: "))

c1 = Calc(v1, v2)

if selection == "1":
    addResult = c1.add()
    print("Add: {}".format(addResult))
    
elif selection == "2":
    sumResult = c1.summ()
    print("Sum: {}".format(sumResult))
    
elif selection == "3":
    mutiplyResult = c1.multiply()
    print("Multiply: {}".format(mutiplyResult))
    
elif selection == "4":
    divisionResult = c1.div()
    print("Division: {}".format(divisionResult))
    
else:
    print("Error. There is no proper selection.")