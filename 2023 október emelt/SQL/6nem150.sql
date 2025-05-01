SELECT nevado, ag, SUM(pontszam) AS osszes
FROM feladatsor, feladat
WHERE feladatsor.id = feladat.feladatsorid
GROUP BY feladat.feladatsorid
HAVING SUM(pontszam) != 150;