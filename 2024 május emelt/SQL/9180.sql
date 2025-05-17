SELECT ingatlan.kozterulet, ingatlan.hazszam, SUM(helyiseg.hossz * helyiseg.szel * IF(helyiseg.funkcio = "terasz", 0.5, 1)) AS terulet
FROM ingatlan, helyiseg
WHERE ingatlan.id = helyiseg.ingatlanid
GROUP BY helyiseg.ingatlanid
HAVING terulet > 180;