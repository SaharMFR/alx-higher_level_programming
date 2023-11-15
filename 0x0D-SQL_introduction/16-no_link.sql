-- Lists all records of the table `second_table` that have a name.
-- Display (score and name) descending ordered by score.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ""
ORDER BY score DESC;
