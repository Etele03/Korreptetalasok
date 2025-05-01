SELECT nevado, COUNT(*) AS db
FROM feladatsor, feladat
WHERE feladatsor.id = feladat.feladatsorid
AND feladat.id NOT IN (
	SELECT feladatid
	FROM megoldas, csapat
	WHERE megoldas.csapatid = csapat.id
	AND nev = "#win"
)
GROUP BY nevado;