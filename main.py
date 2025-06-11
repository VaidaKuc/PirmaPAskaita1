# import random
#
# print("Sveiki")
#
# age = 20
#
# print(age)
#
# name = "Vaida"
# surname = "Kuciauskaite"
#
# print(name + surname)
# print(str(20) + " Skaicius" )
#
# rnd_num = random.randint(4,10)
# print(rnd_num)
#
# if rnd_num == 5:
#     print("musu skaicius yra 5")
#
#     print("zemiau salyginio sakinio")
#
# if rnd_num < 7:
#     print("maziau nei vidurkis")
# elif rnd_num == 7:
#     print("tobulas vidurkis")
# else:
#     print("daugiau nei vidurkis")
#
# print("lasbas, ka tu?")
#
# if 4 > 3 and 6 > 4:
#     print("abi salygos yra teisingos")
#
# if 4 > 3 and 6 > 8:
#   print("bent viena salyga yra teisinga"

vardas = "Vaida"
pavarde = "Kuciauskaite"
gimimo_metai  = 1985
dabar = 2025
amzius = dabar - gimimo_metai

print('As esu' + ' ' + vardas + ' ' + pavarde + '. ' + 'Man yra ' + str(amzius) + ' metu.')
import random

a = random.randint(0, 4)
b = random.randint(0, 4)
print(str(a) + ' ir ' + str(b))
if a == 0 and b == 0:
    print("Dalyba negalima")
elif a == 0 or b == 0:
    print("Dalyba iš nulio negalima")
else:
    didesnis = max(a, b)
    mazesnis = min(a, b)
    rezultatas = didesnis / mazesnis
    print("Rezultatas:", round(rezultatas, 2))


a = random.randint(0, 25)
b = random.randint(0, 25)
c = random.randint(0, 25)
print("Sugeneruotos reikšmės: " + str(a) + ", " + str(b) + ", " + str(c))
skaiciai = [a, b, c]
skaiciai.sort()
vidurine = skaiciai[1]
print("Vidurinė reikšmė: " + str(vidurine))

a = random.randint(0, 10)
b = random.randint(0, 10)
c = random.randint(0, 10)
print("Krastines: a = " + str(a) + ", b = " + str(b) + ", c = " + str(c))
if a + b > c and a + c > b and b + c > a:
    print("Sudaryti trikampio galima")
else:
    print("Sudaryti trikampio negalima")


a = random.randint(0, 2)
b = random.randint(0, 2)
c = random.randint(0, 2)
d = random.randint(0, 2)
nuliai = 0
vienetai = 0
dvejetai = 0
if a == 0:
    nuliai += 1
elif a == 1:
    vienetai += 1
else:
    dvejetai += 1
if b == 0:
    nuliai += 1
elif b == 1:
    vienetai += 1
else:
    dvejetai += 1
if c == 0:
    nuliai += 1
elif c == 1:
    vienetai += 1
else:
    dvejetai += 1
if d == 0:
    nuliai += 1
elif d == 1:
    vienetai += 1
else:
    dvejetai += 1
print("Sugeneruoti skaičiai:", a, b, c, d)
print("Nuliai:", nuliai)
print("Vienetai:", vienetai)
print("Dvejetai:", dvejetai)



a = random.randint(-10, 10)
b = random.randint(-10, 10)
c = random.randint(-10, 10)

if a < 0:
    print("[" + str(a) + "]")
elif a == 0:
    print("(" + str(a) + ")")
else:
    print("{" + str(a) + "}")
if b < 0:
    print("[" + str(b) + "]")
elif c == 0:
    print("(" + str(b) + ")")
else:
    print("{" + str(b) + "}")
if c < 0:
    print("[" + str(c) + "]")
elif c == 0:
    print("(" + str(c) + ")")
else:
    print("{" + str(c) + "}")

kiekis = random.randint(5, 3000)
kaina = 1
nuolaida = 0.0
if kiekis > 2000:
    nuolaida = 0.04
elif kiekis > 1000:
    nuolaida = 0.03
bendra_kaina = kiekis * kaina * (1 - nuolaida)
print("Nupirkta žvakių: " + str(kiekis))
print("Bendra kaina: " + str(round(bendra_kaina, 2)) + " eurų")



a = random.randint(0, 100)#30
b = random.randint(0, 100)#6
c = random.randint(0, 100)#40
print("Sugeneruoti skaičiai:", a, b, c)
vidurkis = round(a + b + c / 3)
print("Vidurkis: " + str(vidurkis))
suma = 0 #+40=70
kiekis = 0 #1+1=2
if 10 <= a <= 90:
    suma += a
    kiekis += 1
if 10 <= b <= 90:
    suma += b
    kiekis += 1
if 10 <= c <= 90:
    suma += c
    kiekis += 1
if kiekis > 0:
    vidurkis_filtruotas = round(suma / kiekis)
else:
    vidurkis_filtruotas = "Nera tinkamu reiksmiu tarp 10 ir 90"
print("vidurkis (visi skaiciai):", vidurkis)

a = random.randint(0,100)
b = random.randint(0,100)
c = random.randint(0,100)
print(a, b, c)
sum = 0
count = 0
if  10 < a < 90:
    sum += a
    count +=1
if  10 < b < 90:
    sum += b
    count +=1
if  10 < c < 90:
    sum += c
    count +=1
print(sum/count)

import datetime
import random
# valandos = random.randint(0, 23)
# minutes = random.randint(0, 59)
# sekundes = random.randint(0, 59)
# pradinis_laikas = datetime.time(valandos, minutes,sekundes)
# print("Pradinis laikas: " + str(pradinis_laikas))
# papildomos_sekundes = random.randint(0, 300)
# print("Pridedamos sekundes: " + str(papildomos_sekundes))
# dabartine_data = datetime.date.today()
# pradinis_datetime = datetime.datetime.combine(dabartine_data, pradinis_laikas)
# sekundziu_timedelta = datetime.timedelta(seconds=papildomos_sekundes)
# po_pridejimo_datetime = pradinis_datetime + sekundziu_timedelta
# galutinis_laikas = po_pridejimo_datetime.time()
# print("Laikas po papildomų sekundžių pridėjimo:", galutinis_laikas)


valandos = random.randint(0, 23)
minutes = random.randint(0, 59)
sekundes = random.randint(0, 59)
print("Pradinis laikas: " + str(valandos) + ":" + str(minutes)+ ":" + str(sekundes))
papildomos_sekundes = random.randint(0, 300)
print("Pridedamos sekundės: " + str(papildomos_sekundes))
sekundes += papildomos_sekundes
if sekundes >= 60:
    papildomos_minutes = sekundes // 60
    sekundes = sekundes % 60
    minutes += papildomos_minutes
if minutes >= 60:
    papildomos_valandos = minutes // 60
    minutes = minutes % 60
    valandos += papildomos_valandos
if valandos >= 24:
    valandos = valandos % 24
print("Laikas po pridėjimo: " + str(valandos)+ ":" + str(minutes)+ ":" + str(sekundes))


# valandos = random.randint(0, 23)
# minutes = random.randint(0, 59)
# sekundes = random.randint(0, 59)
# papildomos_sekundes = random.randint(0, 300)
# viso_sekundziu = valandos * 3600 + minutes * 60 + sekundes
# viso_sekundziu += papildomos_sekundes
# naujos_valandos = (viso_sekundziu // 3600) % 24
# likusios_sekundes = viso_sekundziu % 3600
# naujos_minutes = likusios_sekundes // 60
# naujos_sekundes = likusios_sekundes % 60
# pradinis_laikas = str(valandos).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(sekundes).zfill(2)
# galutinis_laikas = str(naujos_valandos).zfill(2) + ":" + str(naujos_minutes).zfill(2) + ":" + str(naujos_sekundes).zfill(2)
# print("Pradinis laikas:", pradinis_laikas)
# print("Pridedamos sekundės:", papildomos_sekundes)
# print("Laikas po pridėjimo:", galutinis_laikas)

a1 = random.randint(1000, 9999)
a2 = random.randint(1000, 9999)
a3 = random.randint(1000, 9999)
a4 = random.randint(1000, 9999)
a5 = random.randint(1000, 9999)
a6 = random.randint(1000, 9999)
print("Sugeneruoti atsitiktiniai skaičiai:", a1, a2, a3, a4, a5, a6)
rikiuotas = sorted((a1, a2, a3, a4, a5, a6), reverse=True)
rezultatas = str(rikiuotas[0]) + " " + str(rikiuotas[1]) + " " + str(rikiuotas[2]) + " " + str(rikiuotas[3]) + " " + str(rikiuotas[4]) + " " + str(rikiuotas[5])
print("Surūšiuotos reikšmės nuo max:", rezultatas)

import re

word = "otorinolaringologas"

print(len(word))
print(word.upper())
print(word.lower())
print(word.islower())
print(word.replace("o","a"))
print(word.capitalize())
print(word.strip())
print(word[0])
print(word[1])
print(word[2])
print(word[ len(word) -1 ])
print(word[0:5])
print(word[5:10])

print(re.sub("[ao]", "E", word))
print(re.sub("[a-h]", "E", word))

name = "Nicole"
surname = "Kidman"
print(len(name))
print(len(surname))
if name < surname:
    print(name)
else:
    print(surname)

name = "Nicole"
surname = "Kidman"
print(name.upper())
print(surname.lower())

name = "Nicole"
surname = "Kidman"
n_s = name[0] + surname[0]
print(n_s)

name = "Nicole"
surname = "Kidman"
n_s = name[3:6] + surname[3:6]
print(n_s)

name = "An American in Paris"
print(name.replace("a", "*").replace("A", "*"))


name1 = "An American in Paris"
print(re.sub("[a-oA-O]", " ", name1))
name2 = "Breakfast at Tiffany's"
print(re.sub("[a-oA-O]", " ", name2))
name3 = "2001: A Space Odyssey"
print(re.sub("[a-oA-O]", " ", name3))
name4 = "It's a Wonderful Life"
print(re.sub("[a-oA-O]", " ", name4))


starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
epizodas = re.findall(r"\d+", starWars)[0]
print("Epizodo numeris:", epizodas)

starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
print(starWars)
print(starWars[len(starWars) -14])
print(re.sub("[a-zA-Z: -]", " ", starWars))

i = 0
while i < 10:
    i +=1
    print(i)

i = 0
while True:
    i +=1
    if i % 3 == 0:
        continue
    print(i)
    if i >= 50:
        break

my_number = []
for i in range(5):
    my_number.append(random.randint(5, 25))
    print(my_number)

count = 0
for num in my_number:
    if num > 10:
        count += 1
        print("didesniu uz 10 " + str(count))

count = 0
index_counter = 0
for num in my_number:
    index_counter += 1
    if num > 10:
        count += 1
        print("didesniu uz 10 " + str(count))

for index, num in enumerate(my_number):
    print(index, num)

letters = ["A", "B", "C", "D"]
letters[0]
for i in range(20):
    print(letters[random.randint(0, 3)])

print("ciklai")
# 1.Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.
for i in range(10):
    print("labas")

# 2.Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.
for i in range(10):
    print(i)
print("--------")

# 3.Sukurkite masyvą iš dešimties augalų pavadinimų.
augalai = ["rope", "artisokas", "patisonas", "egle", "beržas", "liepa"]
print(augalai)
print("--------")

# 4.Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.
augalai = ["rope", "artisokas", "patisonas", "egle", "beržas", "liepa"]
for augalas in augalai:
           print(augalas)
print("--------")

# 5.Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir baigiant pirmuoju. (atvirkščias ciklas).
augalai = ["rope", "artisokas", "patisonas", "egle", "beržas", "liepa"]
for augalas in reversed(augalai):
           print(augalas)
print("--------")

# 6.Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);
for skaicius in range(10, 51, 2):
    print(skaicius)

print("--------")
# 7. Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius) Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite. ( naudokite continue.) (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)
for skaicius in range(10, 51, 2):
    if skaicius % 10 ==0:
        continue
    print(skaicius)

print("--------")
# 8. Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę;
porinis_skaicius = 0
for i in range(0,21):
    if i % 2 == 0:
        porinis_skaicius += 1
print("Porinių skaičių kiekis:", porinis_skaicius)

print("--------")

# 9. Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai, ir kiek ilgesnių nei 7 simboliai. (du skaičiavimai)
augalai = ["rope", "artisokas", "patisonas", "egle", "beržas", "liepa", "ramunė", "pomidoras"]
žodžiai_5 = 0
žodžiai_7 = 0
for augalas in augalai:
    ilgis = len(augalas)
    if ilgis < 5:
        žodžiai_5 += 1
    if ilgis > 7:
        žodžiai_7 += 1
print("Žodžių trumpesnių nei 5 simboliai:", žodžiai_5)
print("Žodžių ilgesnių nei 7 simboliai:", žodžiai_7)

print("--------")
# 10. Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai. (tarp 5 ir 10 simbolių ilgio)
augalai = ["rope", "artisokas", "patisonas", "egle", "beržas", "liepa", "ramunė", "pomidoras"]
žodis = 0
for augalas in augalai:
    ilgis = len(augalas)
    if ilgis > 5 and ilgis < 10:
        žodis += 1
print("Žodžiai tarp 5 ir 10 simbolių:", žodis)

print("--------")
# 11. Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais ir suskaičiuokite kiek tarp jų yra didesnių už 150.  Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.

import random
skaiciai = [random.randint(0, 300)
        for _ in range(300)]
daugiau_nei_150 = 0
txt = ""
for skaicius in skaiciai:
    if skaicius > 150:
        daugiau_nei_150 += 1
    if skaicius > 275:
        txt += "[" + str(skaicius)+ "] "
        print("[" + str(skaicius)+ "]", end=" ")
    else:
        txt += str(skaicius) + " "
        print(skaicius, end=" ")
print()
print("Skaičių, didesnių už 150 yra:", daugiau_nei_150)

print(txt)

print("--------")

# 12. Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos. Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.

for x in range(1, 3001):
        if x % 77 == 0:
           print(x, end=",")
print()

print("--------")

# Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”

for x in range(25):
    for y in range(25):
        print("*", end="  ")
    print()

print("--------")

# Prieš tai nupieštam kvadratui nupieškite istrižaines zaigzdutę pakeisdami kitu simboliu.

for x in range(25):
    for y in range(25):
        if x == y or x + y == 24:
            print("#", end="  ")
        else:
            print("*", end="  ")
    print()

print("--------")

while True:
    metimas = random.randint(0, 1)
    if metimas == 0:
        print("Herbas")
        break
    else:
        print("Skaičius")
trys_herbai = 0
while True:
    metimas = random.randint(0, 1)
    if metimas == 0:
        print("Herbas")
        trys_herbai += 1
    else:
        print("Skaičius")
    if trys_herbai == 3:
        break
trys_herbai_is_eiles = 0
while True:
    metimas = random.randint(0, 1)
    if metimas == 0:
        print("Herbas")
        trys_herbai_is_eiles += 1
    else:
        print("Skaičius")
        trys_herbai_is_eiles = 0
    if trys_herbai_is_eiles == 3:
        break
print("--------")
# Kazys ir Petras žaidžia šaškėm. Petras surenka taškų kiekį nuo 10 iki 20, Kazys surenka taškų kiekį nuo 5 iki 25.
# Vienoje eilutėje išvesti žaidėjų vardus su taškų kiekiu ir “Partiją laimėjo: ​laimėtojo vardas​”.
# Taškų kiekį generuokite funkcija ​random.randint(x,x)​. Žaidimą laimi tas, kas greičiau surenka 222 taškus.
# Partijas kartoti tol, kol kažkuris žaidėjas pirmas surenka 222 arba daugiau taškų.

petras_taskai = 0
kazys_taskai = 0
while True:
    petro_zaidimas = random.randint(10, 20)
    kazio_zaidimas = random.randint(5, 25)
    petras_taskai += petro_zaidimas
    kazys_taskai += kazio_zaidimas
    print("Petras: " + str(petro_zaidimas) + ", Kazys: " + str(kazio_zaidimas), end=", ")
    if petras_taskai >= 222 and kazys_taskai >= 222:
        if petras_taskai > kazys_taskai:
            print("Partiją laimėjo: Petras")
        elif kazys_taskai > petras_taskai:
            print("Partiją laimėjo: Kazys")
        break
    elif petras_taskai >= 222:
        print("Partiją laimėjo: Petras")
        break
    elif kazys_taskai >= 222:
        print("Partiją laimėjo: Kazys")
        break
    else:
        print()
print("--------")

# Reikia nupaišyti pilnavidurį rombą, taip pat, kaip ir pilnavidurį kvadratą, kurio aukštis 21 eilutė.
for x in range(21):
    for y in range(21):
        print("*", end="  ")
    print()

print("--------")
aukstis = 21
vidurys = aukstis // 2 + 1  # 11
for i in range(1, vidurys + 1):
    tarpai = vidurys - i
    zvaigzdutes = 2 * i - 1
    print(" " * tarpai + "*" * zvaigzdutes)
for i in range(vidurys - 1, 0, -1):
    tarpai = vidurys - i
    zvaigzdutes = 2 * i - 1
    print(" " * tarpai + "*" * zvaigzdutes)

print("--------")

gylis = 0
smugiai = 0
while gylis < 85:
    gylis = gylis + random.randint(5, 15)
    smugiai += 1
print("Smūgis", smugiai, "- įkalta", round(gylis, 2), "mm")
print("Įkalė per:", smugiai, "smūgis")

print("--------")

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_numbers)
print(my_numbers[2])
print(my_numbers[1::2])

empty_list = []
print(empty_list)
empty_list.append(20)
print(empty_list)
empty_list.extend([14, 20, 30])
print(empty_list)

copy = my_numbers.copy()
copy.remove(7)
print(copy)
print(my_numbers)

arr_2d = [
    [1,2,3],
    [2,3,4],
