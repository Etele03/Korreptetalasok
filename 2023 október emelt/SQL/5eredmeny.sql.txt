SELECT nev, SUM(pontszam) AS osszesitett
FROM csapat, megoldas
WHERE csapat.id = megoldas.csapatid
GROUP by csapatid 
ORDER BY osszesitett DESC;