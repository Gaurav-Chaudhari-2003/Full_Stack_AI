# Intermediate SQL Queries

This document explains the intermediate SQL concepts and queries found in `intermediate.sql`.

## 1. GROUP BY and HAVING Clause

The `GROUP BY` statement groups rows that have the same values into summary rows. The `HAVING` clause was added to SQL because the `WHERE` keyword could not be used with aggregate functions.

### Basic Group By
**Count the number of employees in each location.**
```sql
SELECT location, COUNT(*) AS count FROM emp.employee GROUP BY location;
```

### Group By with Multiple Aggregates
**Calculate the count and average score for each job domain, and sort the results by average score in descending order.**
```sql
SELECT job_domain, COUNT(*) AS employees_in_dept, ROUND(AVG(score), 1) AS avg_score
FROM emp.employee
GROUP BY job_domain
ORDER BY avg_score DESC;
```

### Group By with HAVING
**Find the years where more than one employee was hired.**
```sql
SELECT joining_date, COUNT(*) AS employees_hired
FROM emp.employee
GROUP BY joining_date
HAVING employees_hired > 1
ORDER BY employees_hired DESC;
```

### Group By Multiple Columns
**Count the number of employees for each combination of location and job domain.**
```sql
SELECT location, job_domain, COUNT(*) AS count 
FROM emp.employee 
GROUP BY location, job_domain;
```

## 2. Conditional Logic (IF and CASE)

SQL provides functions to perform conditional logic within queries.

### IF Function
**Show 'Promoted' for employees in the sales job domain, and for others show 'Better Luck Next Time'.**
```sql
SELECT emp_name, job_domain, IF(job_domain='sales', 'Promoted', 'Better Luck Next Time') AS status FROM emp.employee;
```

### CASE Statement
**Show 'Promoted' for the sales department, 'Fired' for the marketing department, and 'Better Luck Next Time' for everyone else.**
```sql
SELECT emp_name, job_domain,
       CASE
           WHEN job_domain='sales' THEN 'Promoted'
           WHEN job_domain='marketing' THEN 'Fired'
           ELSE 'Better Luck Next Time'
       END AS job_status
FROM emp.employee;
```

### CASE with Numeric Ranges
**Categorize employee performance based on their score: 'Excellent' for 9 or above, 'Good' for 7 or above, and 'Needs Improvement' for others.**
```sql
SELECT emp_name, score,
       CASE
           WHEN score >= 9 THEN 'Excellent'
           WHEN score >= 7 THEN 'Good'
           ELSE 'Needs Improvement'
       END AS performance
FROM emp.employee;
```

## 3. DDL (Data Definition Language)

DDL commands are used to define the database schema.

### Create Database and Tables
**Create a database named `student` and two tables: `academics` (with student details) and `sports` (linked to academics).**
```sql
CREATE DATABASE IF NOT EXISTS student;

CREATE TABLE IF NOT EXISTS student.academics(
    student_id INT,
    firstname VARCHAR(255),
    remarks VARCHAR(255),
    PRIMARY KEY (student_id)
);

CREATE TABLE IF NOT EXISTS student.sports(
    sport_id INT,
    sport_name VARCHAR(255),
    student_id INT,
    PRIMARY KEY(sport_id),
    FOREIGN KEY(student_id) REFERENCES academics(student_id)
);
```

### Alter Table
**Modify the `academics` table: Add an `address` column, then drop it, and finally rename `firstname` to `first_name`.**
```sql
ALTER TABLE student.academics ADD COLUMN address VARCHAR(255);
ALTER TABLE student.academics DROP COLUMN address;
ALTER TABLE student.academics RENAME COLUMN firstname TO first_name;
```

## 4. DML (Data Manipulation Language)

DML commands are used to manage data within tables.

### Insert, Update, Delete
**Insert a new student record, update an existing student's name, delete a student record, and finally remove all data from the table.**
```sql
-- Insert
INSERT INTO student.academics (student_id, first_name, remarks) VALUES (1, 'A', 'Good');

-- Update
UPDATE student.academics SET first_name = 'Gaurav' WHERE student_id = 2;

-- Delete
DELETE FROM student.academics WHERE student_id = 1;

-- Truncate (Removes all data)
TRUNCATE TABLE student.academics;
```

## 5. String Aggregation

### GROUP_CONCAT
**Concatenate all remarks for each student into a single string.**
```sql
-- Basic usage
SELECT first_name, GROUP_CONCAT(remarks) AS all_remarks 
FROM student.academics 
GROUP BY first_name;
```

**Concatenate remarks for each student, separated by ' | ' and ordered by the remark itself.**
```sql
-- With Ordering and Separator
SELECT first_name, GROUP_CONCAT(remarks ORDER BY remarks DESC SEPARATOR ' | ') AS formatted_remarks
FROM student.academics
GROUP BY first_name;
```

## 6. Cleanup

**Remove the `sports` and `academics` tables, and then drop the `student` database.**
```sql
DROP TABLE IF EXISTS student.sports;
DROP TABLE IF EXISTS student.academics;
DROP DATABASE IF EXISTS student;
```
