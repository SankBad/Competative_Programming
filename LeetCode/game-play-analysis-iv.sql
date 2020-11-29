SELECT ROUND(COUNT(a.player_id)/ (SELECT COUNT(DISTINCT(player_id)) FROM Activity), 2) as fraction
FROM Activity as a,
(SELECT p.player_id, MIN(event_date) as min_event_date FROM Activity as p GROUP BY p.player_id) as b
WHERE a.player_id = b.player_id and a.event_date=b.min_event_date+1
