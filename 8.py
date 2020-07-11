# %% List

liste = [1, 2, 3, 4, 5, 6]
type(liste)

liste_str = ["Pazartesi", "Salı", "Çarşamba"]
type(liste_str)

value = liste[1]
print(value)

last_value = liste[-1]

liste_divide = liste[1:3]

liste.append(7)
liste.remove(7)
liste.reverse()

liste2 = [1, 5, 4, 3, 6, 7, 2]
liste2.sort()

string_int_liste = [1, 2, 3, "cc", "dd"]

# %% Tuple

t = (1, 2, 3, 4, 5, 6)
t.count(3)
t.index(3)

# %% Dictionary

dictionary = {"Ali" : 32, "Veli" : 45, "Ayşe" : 13}

def deneme():
    dictionary = {"Ali" : 32, "Veli" : 45, "Ayşe" : 13}
    return dictionary
dic = deneme()

# %% Conditionals

v1 = 10
v2 = 20

if v1 > v2:
    print("v1 büyüktür v2")
    
elif v1 == v2:
    print("v1 eşittir v2")

else:
    print("v2 büyüktür v1")
    

liste = [1, 2, 3, 4, 5]

v3 = 3

if v3 in liste:
    print("Evet {} değeri listenin içinde.".format(value))
    
else:
    print("Hayır {} değeri listenin içinde değil.".format(value))










