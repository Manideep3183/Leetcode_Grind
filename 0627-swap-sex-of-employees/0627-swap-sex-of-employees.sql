# Write your MySQL query statement below
UPDATE Salary
set sex=CASE
    when sex='m' then 'f'
    else 'm'
END