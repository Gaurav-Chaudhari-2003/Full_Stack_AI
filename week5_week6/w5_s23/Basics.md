# Basic SQL Queries

This document provides an overview of basic SQL queries used in the `Basics.sql` file.

## 1. SELECT Queries

Retrieve data from the `employee` table.

```sql
SELECT * FROM emp.employee;
SELECT emp_id, emp_name FROM emp.employee;
-- Using Aliases for column names
SELECT emp_name AS Name, job_domain AS Department FROM emp.employee;
```

## 2. WHERE Clause

Filter records based on specific conditions.

```sql
SELECT * FROM emp.employee WHERE location = 'maharashtra';
SELECT * FROM emp.employee WHERE job_domain = 'sales';
-- AND Operator
SELECT * FROM emp.employee WHERE location = 'maharashtra' AND job_domain = 'sales';
-- Comparison Operators
SELECT * FROM emp.employee WHERE score >= 8;
SELECT * FROM emp.employee WHERE location != 'Delhi'; -- Not Equal
```

## 3. DISTINCT Clause

Retrieve unique values from a column.

```sql
SELECT DISTINCT location FROM emp.employee;
SELECT DISTINCT job_domain FROM emp.employee;
```

## 4. LIKE Clause

Pattern matching using wildcards.
- `%`: Represents zero or more characters.
- `_`: Represents a single character.

```sql
SELECT * FROM employee WHERE emp_name LIKE 's%';    -- Starts with 's'
SELECT * FROM employee WHERE emp_name LIKE '%a';    -- Ends with 'a'
SELECT * FROM employee WHERE emp_name LIKE '%an%';  -- Contains 'an'
SELECT * FROM employee WHERE emp_name LIKE '__nal'; -- Matches patterns like 'Sonal', 'Minal'
SELECT * FROM employee WHERE emp_name NOT LIKE 'A%'; -- Does not start with 'A'
```

## 5. BETWEEN & AND Clause

Filter records within a specific range.

```sql
SELECT * FROM employee WHERE score > 6 AND score < 9;
SELECT * FROM employee WHERE score BETWEEN 6 AND 9;
-- NOT BETWEEN
SELECT * FROM employee WHERE score NOT BETWEEN 5 AND 8;
-- Date/Year Range
SELECT * FROM employee WHERE joining_date BETWEEN 2010 AND 2020;
```

## 6. IN and OR Clause

Filter records based on multiple values.

```sql
SELECT emp_name, joining_date FROM employee WHERE joining_date = 2000 OR joining_date = 2001 OR joining_date = 2005;
SELECT emp_name, joining_date FROM employee WHERE joining_date IN (2000, 2001, 2005);
-- NOT IN
SELECT * FROM employee WHERE location NOT IN ('Mumbai', 'Pune');
```

## 7. ORDER BY Clause

Sort records in ascending or descending order.

```sql
SELECT * FROM employee WHERE location = 'maharashtra' ORDER BY score DESC;
-- Explicit Ascending
SELECT * FROM employee ORDER BY emp_name ASC;
-- Multiple Column Sorting
SELECT * FROM employee ORDER BY job_domain ASC, score DESC;
```

## 8. LIMIT Clause

Limit the number of records returned.

```sql
SELECT * FROM employee WHERE location = 'maharashtra' ORDER BY score DESC LIMIT 5;
-- Top 3 records
SELECT * FROM employee ORDER BY emp_id LIMIT 3;
```

## 9. OFFSET Clause

Skip a specific number of records.

```sql
SELECT * FROM employee WHERE location = 'maharashtra' ORDER BY score DESC LIMIT 5 OFFSET 1;
```

## 10. COUNT Function

Count the number of records that match a condition.

```sql
SELECT COUNT(*) FROM employee WHERE job_domain = 'marketing';
-- Count Distinct values
SELECT COUNT(DISTINCT job_domain) FROM employee;
```

## 11. Aggregate Functions

Perform calculations on a set of values.

```sql
SELECT MAX(score) FROM employee WHERE job_domain = 'marketing';
SELECT MIN(score) FROM employee WHERE job_domain = 'marketing';
SELECT AVG(score) FROM employee WHERE job_domain = 'marketing';
SELECT ROUND(AVG(score), 1) AS avg_score FROM employee WHERE job_domain = 'marketing';
-- Sum
SELECT SUM(score) FROM employee WHERE job_domain = 'sales';
```

## 12. Optimization

Combine multiple aggregate functions into a single query for better performance.

```sql
SELECT
    MAX(score) AS max_score,
    MIN(score) AS min_score,
    AVG(score) AS avg_score,
    COUNT(*) AS total_employees
FROM employee
WHERE job_domain = 'marketing';
```
