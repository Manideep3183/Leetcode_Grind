# Write your MySQL query statement below
SELECT e.name FROM Employee e
JOIN (
    SELECT managerId FROM Employee 
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) m
on e.id = m.managerId;