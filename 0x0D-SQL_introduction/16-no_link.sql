-- script 16
-- the script  lists all records of the table second_table of the
-- database in a MySQL server.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
