-- #####################################################################
-- # Intermediate SQL Queries
-- #####################################################################

-- #####################################################################
-- # 1. GROUP BY and HAVING Clause
-- #####################################################################

-- Basic Group By
-- Count employees per location
SELECT location, COUNT(*) AS count FROM emp.employee GROUP BY location;

-- Group By with Multiple Aggregates
-- Get employee count and average score per job domain, sorted by average score
SELECT job_domain, COUNT(*) AS employees_in_dept, ROUND(AVG(score), 1) AS avg_score
FROM emp.employee
GROUP BY job_domain
ORDER BY avg_score DESC;

-- Group By with HAVING
-- Find years where more than one employee was hired
SELECT joining_date, COUNT(*) AS employees_hired
FROM emp.employee
GROUP BY joining_date
HAVING employees_hired > 1
ORDER BY employees_hired DESC;

-- Additional Example: Group By with Sum
-- Total score per location
SELECT location, SUM(score) AS total_score FROM emp.employee GROUP BY location;

-- Additional Example: Group By Multiple Columns
-- Count employees by location and job domain
SELECT location, job_domain, COUNT(*) AS count
FROM emp.employee
GROUP BY location, job_domain;

-- #####################################################################
-- # 2. Conditional Logic (IF and CASE)
-- #####################################################################

-- IF Function
-- Show 'Promoted' for sales, otherwise 'Better Luck Next Time'
SELECT emp_name, job_domain, IF(job_domain='sales', 'Promoted', 'Better Luck Next Time') AS status FROM emp.employee;

-- CASE Statement
-- Complex logic: Promoted for sales, Fired for marketing, else Better Luck Next Time
SELECT emp_name, job_domain,
       CASE
           WHEN job_domain='sales' THEN 'Promoted'
           WHEN job_domain='marketing' THEN 'Fired'
           ELSE 'Better Luck Next Time'
       END AS job_status
FROM emp.employee;

-- Additional Example: CASE with Numeric Ranges
-- Categorize scores
SELECT emp_name, score,
       CASE
           WHEN score >= 9 THEN 'Excellent'
           WHEN score >= 7 THEN 'Good'
           ELSE 'Needs Improvement'
       END AS performance
FROM emp.employee;

-- #####################################################################
-- # 3. DDL (Data Definition Language) - Create, Alter, Drop
-- #####################################################################

CREATE DATABASE IF NOT EXISTS student;

-- Create Table with Constraints
-- CHAR vs VARCHAR: CHAR is fixed length, VARCHAR is variable length
CREATE TABLE IF NOT EXISTS student.academics(
    student_id INT,
    firstname VARCHAR(255),
    remarks VARCHAR(255),
    PRIMARY KEY (student_id)
);

-- Create Table with Foreign Key
CREATE TABLE IF NOT EXISTS student.sports(
    sport_id INT,
    sport_name VARCHAR(255),
    student_id INT,
    PRIMARY KEY(sport_id),
    FOREIGN KEY(student_id) REFERENCES academics(student_id)
);

-- Alter Table: Add Column
ALTER TABLE student.academics ADD COLUMN address VARCHAR(255);

-- Alter Table: Drop Column
ALTER TABLE student.academics DROP COLUMN address;

-- Alter Table: Rename Column
ALTER TABLE student.academics RENAME COLUMN firstname TO first_name;

-- #####################################################################
-- # 4. DML (Data Manipulation Language) - Insert, Update, Delete
-- #####################################################################

-- Insert Data
INSERT INTO student.academics (student_id, first_name, remarks) VALUES
(1, 'A', 'Good'),
(2, 'B', 'Good');

-- Update Data
UPDATE student.academics
SET first_name = 'Gaurav'
WHERE student_id = 2;

-- Delete Data
-- Note: SQL_SAFE_UPDATES might need to be disabled for updates/deletes without keys
SET SQL_SAFE_UPDATES = 0;
DELETE FROM student.academics WHERE student_id = 1;

-- Truncate Table (Removes all data but keeps structure)
TRUNCATE TABLE student.academics;

-- Bulk Insert for Testing
INSERT INTO student.academics (student_id, first_name, remarks) VALUES
(1, 'A', 'Good'),
(2, 'B', 'Good'),
(3, 'C', 'BAD'),
(4, 'B', 'Good'),
(5, 'B', 'Good'),
(6, 'A', 'BAD'),
(7, 'B', 'Good'),
(8, 'C', 'Good'),
(9, 'C', 'BAD'),
(10, 'A', 'Good');

-- #####################################################################
-- # 5. String Aggregation
-- #####################################################################

-- GROUP_CONCAT
-- Concatenate remarks for each first_name
SELECT first_name, GROUP_CONCAT(remarks) AS all_remarks, COUNT(*) AS remarks_count
FROM student.academics
GROUP BY first_name;

-- Additional Example: GROUP_CONCAT with Separator and Ordering
SELECT first_name, GROUP_CONCAT(remarks ORDER BY remarks DESC SEPARATOR ' | ') AS formatted_remarks
FROM student.academics
GROUP BY first_name;

-- #####################################################################
-- # Cleanup
-- #####################################################################

-- DROP Tables and Database
DROP TABLE IF EXISTS student.sports;
DROP TABLE IF EXISTS student.academics;
DROP DATABASE IF EXISTS student;
