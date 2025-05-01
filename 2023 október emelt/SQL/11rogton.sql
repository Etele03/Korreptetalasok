SELECT masodik.nevado, masodik.kituzes
FROM feladatsor AS elso, feladatsor AS masodik
WHERE DATEDIFF(masodik.kituzes, elso.hatarido) = 1