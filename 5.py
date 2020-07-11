class Animal():
    
    def __init__(self):
        print("")
        
    def toString(self):   #Overriding
        print("animal")
        
    def walk(self):
        print("")
        
class Monkey(Animal):
    
    def __init__(self):
        super().__init__()
        print("Monkey created.")
        
    def toString(self):
        super().toString()
        print("monkey")
        
    def walk(self):
        super().walk()
        print("Monkey walked.")
        
    def climb(self):
        print("Monkey climbed.")
        
class Bird(Animal):
    
    def __init__(self):
        super().__init__()
        print("Bird created.")
        
    def toString(self):
        print("bird")
        
    def walk(self):
        super().walk()
        print("Bird walked.")
        
    def fly(self):
        print("Bird flied.")
        
monkey1 = Monkey()
monkey1.toString()
monkey1.walk()
monkey1.climb()

print("______________________")

bird1 = Bird()
bird1.toString()
bird1.walk()
bird1.fly()

#%% Inheritance Project 1
class Website():
    "parent"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def loginInfo(self):
        print(self.name + " " + self.surname)
        
class Website1(Website):
    "child"
    def __init__(self, name, surname, ids):
        Website.__init__(self, name, surname)
        #self.name = name
        #self.surname = surname
        self.ids = ids
        
    def login(self):
        print(self.name + " " + self.surname + " " + self.ids)
        
class Website2(Website):
    "child"
    def __init__(self, name, surname, email):
        Website.__init__(self, name, surname)
        #self.name = name
        #self.surname = surname
        self.email = email
        
    def login(self):
        print(self.name + " " + self.surname + " " + self.email)
        
person = Website("name", "surname")
person1  = Website1("Ahmet", "Işık", "12345678")
person2 = Website2("Ayşe", "Şahin", "ayse@gmail")

print("Ana Sitedeki account: ", person.loginInfo())
print("1. Sitedeki account: ", person1.login())
print("2. Sitedeki account: ", person2.login())
print("__________________________________________")
    
# %% Inheritance Project 2
class AnneKedi():
    "parent"
    def __init__(self, sicakkanli, sevimli):
        self.sicakkanli = sicakkanli
        self.sevimli = sevimli
        
    def loginInfo(self):
        print(self.sicakkanli + " ve " + self.sevimli)
        
class YavruKedi1(AnneKedi):
    "child"
    def __init__(self, sicakkanli, sevimli, uysal):
        AnneKedi.__init__(self, sicakkanli, sevimli)
        self.uysal = uysal
        
    def login(self):
        print(self.sicakkanli + " ve " + self.sevimli + " ve " + self.uysal)
        
class YavruKedi2(AnneKedi):
    "child"
    def __init__(self, sicakkanli, sevimli, yaramaz):
        AnneKedi.__init__(self, sicakkanli, sevimli)
        self.yaramaz = yaramaz
        
    def login(self):
        print(self.sicakkanli + " ve " + self.sevimli + " ve " + self.yaramaz)
        
kedi = AnneKedi("sıcakkanlı", "sevimli")
yavru1 = YavruKedi1("sıcakkanlı", "sevimli", "uysal")
yavru2 = YavruKedi2("sıcakkanlı", "sevimli", "yaramaz")

print("Anne Kedi: ", kedi.loginInfo())
print("1. Yavru Kedi: ", yavru1.login())
print("2. Yavru Kedi: ", yavru2.login())
print("__________________________________________")
























