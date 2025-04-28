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

print("Napok\t 1..10\t 11..20\t 21..30")
