# Basic SQL Queries

This document provides an overview of basic SQL queries used in the `Basics.sql` file.

## 1. SELECT Queries

**Retrieve all columns from the `employee` table, then retrieve only the `emp_id` and `emp_name` columns.**
```sql
SELECT * FROM emp.employee;
SELECT emp_id, emp_name FROM emp.employee;
```

**Retrieve `emp_name` as 'Name' and `job_domain` as 'Department' using aliases.**
```sql
-- Using Aliases for column names
SELECT emp_name AS Name, job_domain AS Department FROM emp.employee;
```

## 2. WHERE Clause

**Filter records to show only employees located in 'maharashtra'.**
```sql
SELECT * FROM emp.employee WHERE location = 'maharashtra';
```

**Filter records to show only employees in the 'sales' job domain.**
```sql
SELECT * FROM emp.employee WHERE job_domain = 'sales';
```

**Filter records to show employees who are in 'maharashtra' AND work in 'sales'.**
```sql
-- AND Operator
SELECT * FROM emp.employee WHERE location = 'maharashtra' AND job_domain = 'sales';
```

**Filter records where the score is greater than or equal to 8, or where the location is NOT 'Delhi'.**
```sql
-- Comparison Operators
SELECT * FROM emp.employee WHERE score >= 8;
SELECT * FROM emp.employee WHERE location != 'Delhi'; -- Not Equal
```

## 3. DISTINCT Clause

**Retrieve a list of unique locations and unique job domains from the `employee` table.**
```sql
SELECT DISTINCT location FROM emp.employee;
SELECT DISTINCT job_domain FROM emp.employee;
```

## 4. LIKE Clause

**Find employees whose names start with 's'.**
```sql
SELECT * FROM employee WHERE emp_name LIKE 's%';    -- Starts with 's'
```

**Find employees whose names end with 'a'.**
```sql
SELECT * FROM employee WHERE emp_name LIKE '%a';    -- Ends with 'a'
```

**Find employees whose names contain 'an'.**
```sql
SELECT * FROM employee WHERE emp_name LIKE '%an%';  -- Contains 'an'
```

**Find employees whose names match a pattern like 'Sonal' or 'Minal' (5 letters, ending in 'nal').**
```sql
SELECT * FROM employee WHERE emp_name LIKE '__nal'; -- Matches patterns like 'Sonal', 'Minal'
```

**Find employees whose names do NOT start with 'A'.**
```sql
SELECT * FROM employee WHERE emp_name NOT LIKE 'A%'; -- Does not start with 'A'
```

## 5. BETWEEN and AND Clause

**Find employees with a score strictly between 6 and 9 (exclusive).**
```sql
SELECT * FROM employee WHERE score > 6 AND score < 9;
```

**Find employees with a score between 6 and 9 (inclusive).**
```sql
SELECT * FROM employee WHERE score BETWEEN 6 AND 9;
```

**Find employees with a score NOT between 5 and 8.**
```sql
-- NOT BETWEEN
SELECT * FROM employee WHERE score NOT BETWEEN 5 AND 8;
```

**Find employees who joined between the years 2010 and 2020.**
```sql
-- Date/Year Range
SELECT * FROM employee WHERE joining_date BETWEEN 2010 AND 2020;
```

## 6. IN and OR Clause

**Find employees who joined in 2000, 2001, or 2005 using the OR operator.**
```sql
SELECT emp_name, joining_date FROM employee WHERE joining_date = 2000 OR joining_date = 2001 OR joining_date = 2005;
```

**Find employees who joined in 2000, 2001, or 2005 using the IN operator.**
```sql
SELECT emp_name, joining_date FROM employee WHERE joining_date IN (2000, 2001, 2005);
```

**Find employees who are NOT located in 'Mumbai' or 'Pune'.**
```sql
-- NOT IN
SELECT * FROM employee WHERE location NOT IN ('Mumbai', 'Pune');
```

## 7. ORDER BY Clause

**Retrieve employees in 'maharashtra' and sort them by score in descending order.**
```sql
SELECT * FROM employee WHERE location = 'maharashtra' ORDER BY score DESC;
```

**Retrieve all employees sorted by name in ascending order.**
```sql
-- Explicit Ascending
SELECT * FROM employee ORDER BY emp_name ASC;
```

**Retrieve all employees sorted by job domain (ascending) and then by score (descending).**
```sql
-- Multiple Column Sorting
SELECT * FROM employee ORDER BY job_domain ASC, score DESC;
```

## 8. LIMIT Clause

**Retrieve the top 5 employees in 'maharashtra' with the highest scores.**
```sql
SELECT * FROM employee WHERE location = 'maharashtra' ORDER BY score DESC LIMIT 5;
```

**Retrieve the first 3 employees when sorted by employee ID.**
```sql
-- Top 3 records
SELECT * FROM employee ORDER BY emp_id LIMIT 3;
```

## 9. OFFSET Clause

**Retrieve 5 employees in 'maharashtra' with the highest scores, but skip the first one (the highest).**
```sql
SELECT * FROM employee WHERE location = 'maharashtra' ORDER BY score DESC LIMIT 5 OFFSET 1;
```

## 10. COUNT Function

**Count the total number of employees in the 'marketing' job domain.**
```sql
SELECT COUNT(*) FROM employee WHERE job_domain = 'marketing';
```

**Count the number of unique job domains.**
```sql
-- Count Distinct values
SELECT COUNT(DISTINCT job_domain) FROM employee;
```

## 11. Aggregate Functions

**Find the maximum, minimum, and average score for employees in 'marketing'. Also, calculate the average score rounded to 1 decimal place.**
```sql
SELECT MAX(score) FROM employee WHERE job_domain = 'marketing';
SELECT MIN(score) FROM employee WHERE job_domain = 'marketing';
SELECT AVG(score) FROM employee WHERE job_domain = 'marketing';
SELECT ROUND(AVG(score), 1) AS avg_score FROM employee WHERE job_domain = 'marketing';
```

**Calculate the total sum of scores for employees in 'sales'.**
```sql
-- Sum
SELECT SUM(score) FROM employee WHERE job_domain = 'sales';
```

## 12. Optimization

**Retrieve the maximum, minimum, and average score, along with the total count of employees in 'marketing', all in a single query.**
```sql
SELECT
    MAX(score) AS max_score,
    MIN(score) AS min_score,
    AVG(score) AS avg_score,
    COUNT(*) AS total_employees
FROM employee
WHERE job_domain = 'marketing';
```
