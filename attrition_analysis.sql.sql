CREATE DATABASE employee_attrition_project;
USE employee_attrition_project;
select * from employees;

/* Total Employees */
## Counts total number of employees in the dataset. (" This gives the base population for attrition analysis.")
select count(*) as total_employees from employees;

/* Attrition Count */
## Groups employees into Yes (left) and No (stayed) and counts them. ("Helps understand overall employee turnover.")
select attrition, count(*) as employee_count
from employees
group by attrition;

/* Attrition Percentage */
## Calculates percentage of employees who left. (" Gives attrition rate used in business reporting.")
select 
count(case when attrition ="Yes" then 1 end) * 100.0/count(*) as attrition_percentage from employees;


/* Attrition by Department*/
# Filters employees who left and counts them department-wise.('Identifies departments with high attrition.')
select 
department, count(*) as attrition_count
from employees
where attrition ="Yes"
Group By department
order by attrition_count desc;


/*   Average Salary by Attrition*/
# Compares average salary between employees who left and stayed. ( Helps understand if low salary influences attrition.)
select attrition, avg(salary) as average_salary
from employees
group by attrition;

/* Average Experience by Attrition*/
## Compares experience levels between employees who left and stayed.  (Shows whether new employees leave more.)
select attrition, avg(years_at_company) as avg_years_at_company
from employees
group by attrition;

/* Performance Score Analysis*/
# Compares performance of employees who left vs stayed.(Identifies if attrition is related to performance.)
select attrition, Avg(performance_score) as avg_performance_score
from employees
group by attrition;

/* Attrition by Gender*/
# Counts attrition across gender.(Shows distribution of attrition across genders.)
select gender, count(*) as attrition_count
from employees
where attrition = "Yes"
group by gender;

/* Attrition by Age Group*/
# Groups employees into age categories and counts attrition. (Helps identify which age group leaves more.)
select case 
when  age between 20 and 29 then '20-29'
when age between 30 and 39 then '30-39'
when age between 40 and 49 then '40-49'
else '50+'
end as age_group,
count(*) as attrition_count
from employees
where attrition ='yes'
group by age_group
order by attrition_count desc;