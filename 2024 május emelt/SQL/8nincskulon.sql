SELECT kozterulet, hazszam
FROM ingatlan
WHERE id NOT IN (	SELECT helyiseg.id
                	From helyiseg
                	WHERE helyiseg.funkcio = "konyha")
	AND id NOT IN (SELECT helyiseg.id
                  FROM helyiseg
                  WHERE helyiseg.funkcio = "WC");