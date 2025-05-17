SELECT jatekos.nev, bajnok.ev, versenyszam.nev
FROM jatekos, bajnok, versenyszam
WHERE jatekos.id = bajnok.jatekos_id AND bajnok.vsz_id = versenyszam.id
	AND jatekos.id IN (	SELECT bajnok.jatekos_id
                        FROM bajnok
                        GROUP BY bajnok.jatekos_id
                        HAVING COUNT(*) = 1);