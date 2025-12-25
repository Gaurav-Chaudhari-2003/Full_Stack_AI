#TABLE RELATED
SELECT * FROM emp.employee;

USE emp;
SELECT * FROM employee;

SELECT emp_id, emp_name FROM employee;

#WHERE QUERY
SELECT * FROM employee WHERE location='Maharashtra';
SELECT * FROM employee WHERE job_domain='sales';
SELECT * FROM employee WHERE score = 5;
SELECT * FROM employee WHERE location='maharashtra' AND job_domain='sales';

#DISTINCT QUERY
SELECT DISTINCT location FROM employee;
SELECT DISTINCT score FROM employee;

#LIKE QUERY
SELECT * FROM employee WHERE emp_name LIKE 's%';
SELECT * FROM employee WHERE emp_name LIKE '%ar%';
SELECT * FROM  employee WHERE score LIKE '7%';

#AND & BETWEEN
SELECT * FROM employee WHERE score>9;
SELECT * FROM employee WHERE score>6;

SELECT * FROM employee WHERE score>=6 AND score<=9;
SELECT * FROM employee WHERE score BETWEEN 6 AND 9;


#OR & IN
SELECT emp_id, emp_name FROM employee WHERE joining_date=2000 OR joining_date=2001 OR joining_date=2005;
SELECT emp_id, emp_name FROM employee WHERE joining_date IN(2000,2001,2005);

SELECT * FROM employee WHERE score BETWEEN 9 AND 10 OR joining_date IN(2001,2002,2003);

#ORDER BY, DESC, LIMIT & OFFSET
SELECT * FROM employee WHERE location = 'maharashtra' ORDER BY score;
SELECT * FROM employee WHERE location = 'maharashtra' ORDER BY score DESC;
SELECT * FROM employee WHERE location = 'maharashtra' ORDER BY score DESC LIMIT 5;
SELECT * FROM employee WHERE location = 'maharashtra' ORDER BY score DESC LIMIT 5 OFFSET 1;     #OFFSET: SKIPS THE FIRST N ROWS
SELECT * FROM employee WHERE joining_date BETWEEN 1990 AND 2000 ORDER BY score DESC LIMIT 5 OFFSET 3;

#COUNT
SELECT count(*) FROM employee WHERE job_domain="marketing";
SELECT COUNT(*) FROM employee WHERE score >= 9;

#MAX,MIN,AVG
SELECT max(score) FROM employee WHERE job_domain= 'marketing';
SELECT min(score) FROM employee WHERE job_domain= 'marketing';
SELECT avg(score) FROM employee WHERE job_domain= 'marketing';
SELECT round(avg(score),1) FROM employee WHERE job_domain= 'marketing';         #ROUND: ROUNDS THE NUMBER TO 1 DECIMAL PLACE
SELECT ROUND(AVG(score), 2) FROM employee;

SELECT max(score) as max_score,
	   min(score) as min_score,
       round(avg(score),1) as avg_score
 from employee 
 WHERE job_domain= 'marketing';
 
#GROUP BY
 SELECT location, count(location) FROM employee group by location;
 
 SELECT job_domain, count(job_domain) as domain_count,round(avg(score),1) as avg_score
 FROM employee
 group by job_domain 
 order by avg_score desc;
 
#HAVING
 SELECT
           joining_date,
           count(*) as date_count
	FROM employee
	group by joining_date
	having date_count>1
	order by date_count desc;
    
#IF QUERY   
 SELECT
	emp_name,
	if (job_domain='sales', 'PROMOTED', 'NEXT TIME PAKKA') as job_status 
	FROM employee;
    
#CASE QUERY    
    SELECT
	emp_name,
	case
		when job_domain='sales' then'PROMOTED'
		when job_domain='marketing' then'FIRED'
		else 'NEXT TIME PAKKA'
		end
        as job_status
    FROM employee;


















