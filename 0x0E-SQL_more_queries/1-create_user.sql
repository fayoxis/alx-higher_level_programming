-- script 1
-- this will  create the MySQL server for the  user user_0d_1.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
