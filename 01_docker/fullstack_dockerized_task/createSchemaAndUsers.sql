CREATE SCHEMA casedb;
CREATE USER 'jyser3'@'localhost' IDENTIFIED BY 'SOME_SAFE_PASSWORD_YOU_WRITE_DOWN';
GRANT ALL ON casedb.* TO 'jyser3'@'localhost' WITH GRANT OPTION;