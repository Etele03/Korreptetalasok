SELECT ingatlan.kozterulet, ingatlan.hazszam, hirdet.ar
FROM ingatlan, hirdetes AS hirdet, hirdetes AS elad
WHERE ingatlan.id = hirdet.ingatlanid
	AND hirdet.ingatlanid = elad.ingatlanid
    AND hirdet.allapot = "meghirdetve"
    AND elad.allapot = "eladva"
    AND hirdet.ar = elad.ar;