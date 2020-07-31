# Write your MySQL query statement below
SELECT table1.FirstName, table1.LastName, table2.City, table2.State
FROM Person as table1 LEFT JOIN Address as table2
ON table1.PersonID = table2.PersonID
