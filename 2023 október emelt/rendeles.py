# 1. feladat

adatok = []

with open("rendel.txt", "r", encoding="utf-8") as file:
    for sor in file:
        adatok.append(sor.strip().split(" "))

# 2. feladat
print("2. feladat:")

print(f"A rendelések száma: {len(adatok)}")

# 3. feladat
print("3. feladat:")


nap = input("Kérem, adjon meg egy napot: ")
db = 0

for sor in adatok:
    if sor[0] == nap:
        db += 1
print(f"A rendelések száma az adott napon: {db}")

# 4. feladat
print("4. feladat:")

volt_rendeles = []

for sor in adatok:
    if sor[1] == "NR" and sor[0] not in volt_rendeles:
        volt_rendeles.append(sor[0])

if len(volt_rendeles) == 30:
    print("Minden nap volt rendelés a reklámban nem érintett városból")
else:
    print(f"{30 - len(volt_rendeles)} nap nem volt a reklámban nem érintett városból rendelés")
    
# 5. feladat
print("5. feladat:")

legnagyobb = '0'

for sor in adatok:
    if legnagyobb < sor[2]:
        legnagyobb = sor[2]

for sor in adatok:
    if legnagyobb == sor[2]:
        print(f"A legnagyobb darabszám: {legnagyobb}, a rendelés napja: {sor[0]}")
        break

# 6. feladat

def osszes(varos, nap):
    ossz = 0

    for sor in adatok:
        if varos == sor[1] and nap == int(sor[0]):
            ossz += int(sor[2])
    
    return ossz

#print(f"{osszes('PL', 7)} ")

# 7. feladat
print("7. feladat:")

n = 21

print(f"A rendelt termékek darabszáma a {n}. napon PL: {osszes('PL', n)} TV: {osszes('TV', n)} NR: {osszes('NR', n)}")


# 8. feladat
print("8. feladat:")



with open("kampany.txt", "w", encoding="utf-8") as file:
    file.write("Napok\t 1..10\t 11..20\t 21..30\n")
    print("Napok\t 1..10\t 11..20\t 21..30")

    elso = []
    masodik = []
    harmadik = []

    # elso sor

    for sor in adatok:
        if 1 <= int(sor[0]) <= 10 and sor[1] == 'PL':
            elso.append(sor[0])

    for sor in adatok:
        if 11 <= int(sor[0]) <= 20 and sor[1] == 'PL':
            masodik.append(sor[0])

    for sor in adatok:
        if 21 <= int(sor[0]) <= 30 and sor[1] == 'PL':
            harmadik.append(sor[0])

    file.write(f"PL\t {len(elso)}\t {len(masodik)}\t {len(harmadik)}\n")
    print(f"PL\t {len(elso)}\t {len(masodik)}\t {len(harmadik)}")
    elso.clear()
    masodik.clear()
    harmadik.clear()

    # masodik sor

    for sor in adatok:
        if 1 <= int(sor[0]) <= 10 and sor[1] == 'TV':
            elso.append(sor[0])

    for sor in adatok:
        if 11 <= int(sor[0]) <= 20 and sor[1] == 'TV':
            masodik.append(sor[0])

    for sor in adatok:
        if 21 <= int(sor[0]) <= 30 and sor[1] == 'TV':
            harmadik.append(sor[0])

    file.write(f"TV\t {len(elso)}\t {len(masodik)}\t {len(harmadik)}\n")
    print(f"TV\t {len(elso)}\t {len(masodik)}\t {len(harmadik)}")
    elso.clear()
    masodik.clear()
    harmadik.clear()

    # harmadik sor

    for sor in adatok:
        if 1 <= int(sor[0]) <= 10 and sor[1] == 'NR':
            elso.append(sor[0])

    for sor in adatok:
        if 11 <= int(sor[0]) <= 20 and sor[1] == 'NR':
            masodik.append(sor[0])

    for sor in adatok:
        if 21 <= int(sor[0]) <= 30 and sor[1] == 'NR':
            harmadik.append(sor[0])

    file.write(f"NR\t {len(elso)}\t {len(masodik)}\t {len(harmadik)}\n")
    print(f"NR\t {len(elso)}\t {len(masodik)}\t {len(harmadik)}")
    elso.clear()
    masodik.clear()
    harmadik.clear()