# %% Encapsullation

class BankAccount:
    
    def __init__(self, name, money, address):
        self.name = name
        self.adress = address
        self.__money = money
        
    def getMoney(self):
        return self.__money
    
    def setMoney(self, amount):
        self.__money = amount
    
    def __increase(self):
        self.__money = self.__money + 1000
        
h1 = BankAccount("Ali", 1000, "Ümraniye")
h2 = BankAccount("Mehmet", 2000, "Ataşehir")

print("get method: ", h1.getMoney())
print("get method: ", h2.getMoney())

h1.setMoney(2000)
h2.setMoney(3000)

print("After set method: ", h1.getMoney())
print("After set method: ", h2.getMoney())

h1.__increase(1000)
h2.__increase(1000)

print("After increase method: ", h1.getMoney())
print("After increase method: ", h2.getMoney())