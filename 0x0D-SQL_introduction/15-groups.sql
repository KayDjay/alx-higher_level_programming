-- List the number with records with the same score value
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score
ORDER BY number DESC
