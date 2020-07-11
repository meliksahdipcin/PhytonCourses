class DaireToplamAlan():
    r1 = 2
    r2 = 3
    pi = 3.14
    def ToplamAlan(self):
        a = self.r1 ** 2 * self.pi
        b = self.r2 ** 2 * self.pi
        c = a + b
        print("1. daire alanı =", a)
        print("2. daire alanı =", b)
        print("Toplam daire alanı =", c)
D = DaireToplamAlan()
D.ToplamAlan()

def ToplamAlan(r1, r2, pi):
    toplam = (r1 ** 2 * pi) + (r2 ** 2 * pi)
    print("Toplam Daire Alanı =", toplam)
ToplamAlan(2, 3, 3.14)

#%% Initilazer or Contructor

class Animal():
    
    def __init__(self, x, y):
        self.name = x
        self.age = y
        
    def getName(self):
        print("")
        return self.name
    
    def getAge(self):
        print("")
        return self.age
    
a1 = Animal("dog", 5)
a2 = Animal("cat", 6)
a3 = Animal("bird", 2)
a4 = Animal("fish", 1)

print("1st animal name =", a1.getName())
print("2nd animal name =", a2.getName())
print("3rd animal name =", a3.getName())
print("4th animal name =", a4.getName())

print("1st animal age =", a1.getAge())
print("2nd animal age =", a2.getAge())
print("3rd animal age =", a3.getAge())
print("4th animal age =", a4.getAge())

#%% Ödev

class School():
    
    def __init__(self, x, y):
        self.name = x
        self.number = y
        
    def  getName(self):
        print("")
        return self.name
    def  getNumber(self):
        print("")
        return self.number
    
s1 = School("Melikşah", 362)
s2 = School("Ada", 838)
s3 = School("Aydın", 786)
s4 = School("Lerzan", 673)
s5 = School("Emrecan", 862)

print("1st student name =", s1.getName())
print("1st student number =", s1.getNumber())
print("2nd student name =", s2.getName())
print("2nd student number =", s2.getNumber())
print("3rd student name =", s3.getName())
print("3rd student number =", s3.getNumber())
print("4th student name =", s4.getName())
print("4th student number =", s4.getNumber())
print("5th student name =", s5.getName())
print("5th student number =", s5.getNumber())
