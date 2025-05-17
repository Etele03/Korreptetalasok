SELECT DISTINCT jatekos.nev
FROM jatekos, bajnok, versenyszam
WHERE jatekos.id = bajnok.jatekos_id AND bajnok.vsz_id = versenyszam.id
	AND jatekos.nev <> "Pergel Szandra"
    AND versenyszam.nev = "vegyes páros"
    AND bajnok.ev IN (	SELECT bajnok.ev
                        FROM jatekos, bajnok, versenyszam
                        WHERE jatekos.id = bajnok.jatekos_id AND bajnok.vsz_id = versenyszam.id
                            AND jatekos.nev = "Pergel Szandra"
                            AND versenyszam.nev = "vegyes páros");