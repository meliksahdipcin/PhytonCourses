# %% Loops

# for
for each in range(1, 11):
    print(each)
    
for each in "Ankara Istanbul":
    print(each)
    
for each in "Ankara Istanbul".split():
    print(each)
    
liste = [1, 4, 5,6 ,8, 3, 3, 4, 67]
summation = sum(liste)

count = 0
for each in liste:
    count = count + each
    print(count)
    
# while
i = 0
while i < 4:
    print(i)
    i = i + 1
    
sinir = len(liste)
each = 0
count = 0
while each < sinir:
    count = count + liste[each]
    each = each + 1
    print(count)
    print(each)
    print(sinir)
    
# %%

liste = [1, 2, 3, 4, 5, 6, 423, 67, 21, -500, 541, 67]

mini = 10000
for each in liste:
    if each < mini:
        mini = each
    else:
        continue
print(mini)

# %%

class Calisan():
    zamOrani = 0.18
    counter = 0
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.email = ad + soyad + "@asd.com"
        
        Calisan.counter = Calisan.counter + 1
        
    def adSoyadVer(self):
        return self.ad + " " + self.soyad
    
    def zamYap(self):
        self.maas = self.maas + self.maas * self.zamOrani
        
isci1 = Calisan("Ahmet", "Kartal", 3000)
print(isci1.maas)
print(isci1.adSoyadVer())

calisan1 = Calisan("Ahmet", "Demir", 4000)
print("Adı soyadı: ", calisan1.adSoyadVer())
print("Email: ", calisan1.email)
print("İlk maaş: ", calisan1.maas)
calisan1.zamYap()
print("Yeni maaş: ", calisan1.maas)

# %%

class Sirket():
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
    
    def adSoyadVer(self):
        return self.ad + " " + self.soyad
    
gorevli1 = Sirket("Melikşah", "Dipçin", 395000)
gorevli2 = Sirket("Steve", "Jobs", 95000)
gorevli3 = Sirket("Tim", "Cook", 5000)
gorevli4 = Sirket("Johny", "Ive", 5000)
gorevli5 = Sirket("Walter", "White", 10000)
gorevli6 = Sirket("Donald", "Trump", 295000)
gorevli7 = Sirket("Luis Fonsi", "Dipçin", 7000)
gorevli8 = Sirket("Camila", "Cabello", 6000)
gorevli9 = Sirket("Isaac", "Asimov", 5000)
gorevli10 = Sirket("Hector", "Garcia", 4000)

liste = [gorevli1, gorevli2 gorevli3, gorevli4, gorevli5, gorevli6, gorevli7, gorevli8, gorevli9, gorevli10] 
maxiMaas = -1
index = -1

for each in liste:
    if each.maas > maxiMaas:
        maxiMaas = each.maas
        index = each
        
print(maxiMaas)
print(index.adSoyadVer())
































