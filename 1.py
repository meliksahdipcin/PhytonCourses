string = "Anabilim"
integer = 1987

ogrYas = 15
ogrAd = "Rana"
ogrAdres = "SASALJSNLKNDA"

#%% classes

class Fen10():
    Name = "Ege"
    MatNot = 85
    TarNot = 90
    MatNot2 = 95
    TarNot2 = 90
    Name2 = Ada
    
ogr1 = Fen10()
ogr2 = Fen10()

print(ogr1)
print(ogr1.Name)
print(ogr1.MatNot)
print(ogr1.TarNot)

print(ogr2)
print(ogr2.Name2)
print(ogr2.MatNot2)
print(ogr2.TarNot2)

ogr1.MatNot = 100
print(ogr1)
print(ogr1.Name)
print(ogr1.MatNot)
print(ogr1.TarNot)

#%% class example

class Square():
    edge = 5
    area = 0
    
    def alanBul(self):
        self.area = self.edge * self.edge # area = edge **2 (egde kare)
        print("Alan =", self.area)
        
s1 = Square()
print("Bir kenarın uzunluğu =", s1.edge)
print(s1.alanBul())
