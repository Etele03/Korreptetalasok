SELECT ingatlan.kozterulet, ingatlan.hazszam, hirdetes.datum
FROM hirdetes, ingatlan
WHERE hirdetes.ingatlanid = ingatlan.id
GROUP BY hirdetes.ingatlanid
HAVING COUNT(*) = 1
ORDER BY hirdetes.datum
LIMIT 1;