# 1. feladat

adatok = []

with open("taborok.txt", "r", encoding="utf-8") as file:
    for sor in file:
        adatok.append(sor.strip().split("\t"))



print("2. feladat")
print(f"Az adatsorok száma: {len(adatok)}")


print("3. feladat")
van = False

for sor in adatok:
    if sor[-1] == "zenei":
        print(f"Zenei tábor kezdődik {sor[0]}. hó {sor[1]}. napján. ")
        van = True
    
if van == False:
    print("„Nem volt zenei tábor.")

print("4. feladat")
print("Legnépszerűbbek:")

mennyi = 0

for sor in adatok:
    if len(sor[4]) > mennyi:
        mennyi = len(sor[4])

for sor in adatok:
    if len(sor[4]) == mennyi:
        print(f"{sor[0]} {sor[1]} {sor[-1]}")

# 5. feladat

def sorszam(honap, nap):
    if honap == 6:
        return nap - 15
    if honap == 7:
        return nap + 15
    return nap + 46

print("6. feladat")

ho  = int(input("hó: "))
n  = int(input("nap: "))

db = 0

for sor in adatok:
    if sorszam(int(sor[0]), int(sor[1])) <= sorszam(ho, n) and sorszam(ho, n) <= sorszam(int(sor[2]), int(sor[3])):
        db += 1

print(f"Ekkor éppen {db} tábor tart.")

print("7. feladat")

tanulo = input("Adja meg egy tanuló betűjelét: ")
resztvetel = []

for sor in adatok:
    if tanulo in sor[4]:
        resztvetel.append(sor)


for i in range(len(resztvetel)-1):
    for j in range(len(resztvetel)-1):
        if sorszam(int(resztvetel[j][0]), int(resztvetel[j][1])) > sorszam(int(resztvetel[j+1][0]), int(resztvetel[j+1][1])):
            resztvetel[j], resztvetel[j+1] = resztvetel[j+1], resztvetel[j]

with open("egytanulo.txt", "w", encoding="utf-8") as file:
    for sor in resztvetel:
        file.write(f"{sor[0]}.{sor[1]}-{sor[2]}.{sor[3]}. {sor[-1]}\n")

tudmenni = True

for i in range(len(resztvetel)-1):
    if sorszam(int(resztvetel[i+1][0]), int(resztvetel[i+1][1])) <= sorszam(int(resztvetel[i][2]), int(resztvetel[i][3])):
        tudmenni = False

if tudmenni == True:
    print("tudmenni")
else:
    print("nem tud menni")
