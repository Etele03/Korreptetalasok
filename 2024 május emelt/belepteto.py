# 1. feladat

adatok = []

with open("bedat.txt", "r", encoding="utf-8") as file:
    for sor in file:
        adatok.append(sor.strip().split(" "))

# 2. feladat
print("2. feladat")

print(f"Az első tanuló {adatok[0][1]}-kor lépett be a főkapun.")
print(f"Az utolsó tanuló {adatok[len(adatok)-1][1]}-kor lépett ki a főkapun.")      # adatok[-1] is jó

# 3. feladat

with open("kesok.txt", "w", encoding="utf-8") as file:
    for sor in adatok:
        if "07:50" < sor[1] <= "08:15" and sor[2] == "1" :
            file.write(f"{sor[1]} {sor[0]}\n")

# 4. feladat
print("4. feladat")

db = 0

for sor in adatok:
    if sor[2] == "3":
        db += 1

print(f"A menzán aznap {db} tanuló ebédelt.")

# 5. feladat
print("5. feladat")

konyvtarban = []

for sor in adatok:
    if sor[2] == "4" and sor[0] not in konyvtarban:
        konyvtarban.append(sor[0])


print(f"Aznap {len(konyvtarban)} tanuló kölcsönzött a könyvtárban.")

if len(konyvtarban) > db:
    print("Többen voltak, mint a menzán.")
else:
    print("Nem voltak többen, mint a menzán.")

# 6. feladat
print("6. feladat")

iskolaban = []

for sor in adatok:
    if sor[2] == "1":
        iskolaban.append(sor[0])
    elif sor[2] == "2":
        iskolaban.pop(iskolaban.index(sor[0]))

print("Az érintett tanulók:")
#print(*iskolaban, sep=" ")              #alapból a sep szóköz

for i in iskolaban:
    print(i, end=" ")

print("\n")


# 7. feladat
print("7. feladat")

id = input("Egy tanuló azonosítója=")

erkezes = "ures"

for sor in adatok:
    if sor[0] == id and sor[2] == "1":
        erkezes = sor[1]
        break

if erkezes == "ures":
    print("Ilyen azonosítójú tanuló aznap nem volt az iskolában.")
else:
    tavozas = "ures"

    for sor in adatok[::-1]:
        if sor[0] == id and sor[2] == "2":
            tavozas = sor[1]
            break
    
    erkezes = erkezes.split(":")
    tavozas = tavozas.split(":")

    erkezes_perc = int(erkezes[0]) * 60 + int(erkezes[1])
    tavozas_perc = int(tavozas[0]) * 60 + int(tavozas[1])

    mennyi_perc = tavozas_perc - erkezes_perc
    mennyi_ora = mennyi_perc // 60
    mennyi_perc = mennyi_perc % 60

    print(f"A tanuló érkezése és távozása között {mennyi_ora} óra {mennyi_perc} perc telt el.")

