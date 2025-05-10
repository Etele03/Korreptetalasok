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

ho = int(input("hó: "))
n = int(input("nap: "))

db = 0

for sor in adatok:
    if sorszam(int(sor[0]), int(sor[1])) <= sorszam(ho, n) and sorszam(ho, n) <= sorszam(int(sor[2]), int(sor[3])):
        db += 1


print(f"Ekkor éppen {db} tábor tart.")



print("7. feladat")

tanulo = input("Adja meg egy tanuló betűjelét: ")
reszvetel = []

# megkeresem a tanulo betut a taborokban és elmentem egy masik listbe

for sor in adatok:
    if tanulo in sor[-2]:
        reszvetel.append(sor)

# sorba rakom a táborokat kezdés alapján

for i in range(len(reszvetel) - 1):
    for j in range(len(reszvetel) - 1):
        if sorszam(int(reszvetel[j][0]), int(reszvetel[j][1])) > sorszam(int(reszvetel[j+1][0]), int(reszvetel[j+1][1])):
            reszvetel[j], reszvetel[j+1] = reszvetel[j+1],  reszvetel[j]

# kiiratom txt-be

with open("egytanulo.txt" , "w", encoding="utf-8") as file:
    for r in reszvetel:
        file.write(f"{r[0]}.{r[1]}-{r[2]}.{r[3]}. {r[-1]}\n")


# megnézem tud e menni az összesre

tudmenni = True

# hátra fele vizsgál
for i in range(1,  len(reszvetel)):
    if sorszam(int(reszvetel[i][0]), int(adatok[i][1])) <= sorszam(int(reszvetel[i-1][2]), int(adatok[i-1][3])):
        tudmenni = False

#előre vizsgál
for i in range(len(reszvetel) - 1):
    if sorszam(int(reszvetel[i+1][0]), int(adatok[i+1][1])) <= sorszam(int(reszvetel[i][2]), int(adatok[i][3])):
        tudmenni = False

if tudmenni:
    print("Részt tud venni mindegyik táborban:")
else:
    print("Nem mehet el mindegyik táborba.")