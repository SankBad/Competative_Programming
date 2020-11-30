SELECT a.Name
FROM Employee as a,
(SELECT p.ManagerId as Id, COUNT(*) as cnt FROM Employee as p GROUP BY p.ManagerId) as man_cnt
WHERE a.ID=man_cnt.Id and man_cnt.cnt>4
