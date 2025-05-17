import matplotlib.pyplot as plt
from math import atan2

# Pont osztály
class Pont:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"({self.x}, {self.y})"

# Forgásirány meghatározása: pozitív = balra
def forgasirany(p0, p1, p2):
    return (p1.x - p0.x) * (p2.y - p0.y) - (p1.y - p0.y) * (p2.x - p0.x)

# Pontok rendezése polárszög szerint
def polarszog_szerint_rendez(pontok, p0):
    def kulcs(p):
        szog = atan2(p.y - p0.y, p.x - p0.x)
        tav = (p.y - p0.y)**2 + (p.x - p0.x)**2
        return (szog, tav)
    return sorted(pontok, key=kulcs)

# Graham-pásztázás algoritmus
def graham_pasztazas(Q):
    # Kiindulópont meghatározása
    P0 = min(Q, key=lambda p: (p.y, p.x))
    # Rendezés polárszög szerint
    P = polarszog_szerint_rendez(Q, P0)
    # Verem inicializálása első 3 ponttal
    S = [P[0], P[1], P[2]]
    # Pontok feldolgozása és konvex burok építése
    for i in range(3, len(P)):
        while len(S) >= 2 and forgasirany(S[-2], S[-1], P[i]) <= 0:
            S.pop()
        S.append(P[i])
    return S

# Tesztadatok
pontok = [
    Pont(0, 3), Pont(1, 1), Pont(2, 2), Pont(4, 4),
    Pont(0, 0), Pont(1, 2), Pont(3, 1), Pont(3, 3)
]

# Konvex burok meghatarozása
burok = graham_pasztazas(pontok)

# Eredmény kiírás
print("Konvex burok pontjai:")
for p in burok:
    print(p)

# Ábrázolás
def abrazol(pontok, burok):
    x = [p.x for p in pontok]
    y = [p.y for p in pontok]
    plt.plot(x, y, 'o', label='Pontok')

    hx = [p.x for p in burok] + [burok[0].x]
    hy = [p.y for p in burok] + [burok[0].y]
    plt.plot(hx, hy, 'r-', linewidth=2, label='Konvex burok')

    plt.title("Graham-pásztázás")
    plt.grid(True)
    plt.legend()
    plt.show()

abrazol(pontok, burok)
