SELECT a.person_name
FROM Queue as a, Queue as b
WHERE a.turn<b.turn 
GROUP BY a.turn
HAVING sum(a.weight)<1000
ORDER BY a.turn DESC
LIMIT 1
