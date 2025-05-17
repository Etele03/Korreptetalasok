SELECT jatekos.nev, MAX(bajnok.ev) - MIN(bajnok.ev)
FROM jatekos, bajnok
WHERE jatekos.id = bajnok.jatekos_id
GROUP BY jatekos.id
HAVING MAX(bajnok.ev) - MIN(bajnok.ev) >= 10
ORDER BY 2 DESC;