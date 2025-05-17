SELECT ingatlan.hazszam, hirdetes.ar
FROM hirdetes, ingatlan
WHERE hirdetes.ingatlanid = ingatlan.id
	AND hirdetes.allapot = "meghirdetve"
    AND ingatlan.kozterulet = "Agyagos utca";