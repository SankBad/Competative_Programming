SELECT distinct(b.page_id) as recommended_page
FROM
(SELECT
CASE 
WHEN user1_id = 1 THEN user2_id
WHEN user2_id = 1 THEN user1_id
END as friend_1
FROM Friendship) as a, Likes as b
WHERE a.friend_1 = b.user_id
AND b.page_id not in (SELECT page_id from Likes where user_id=1)
