SELECT MIN(bajnok.ev) AS elso
FROM versenyszam, bajnok
WHERE versenyszam.id = bajnok.vsz_id
	AND versenyszam.nev = "vegyes páros";