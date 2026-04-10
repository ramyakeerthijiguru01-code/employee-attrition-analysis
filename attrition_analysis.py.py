# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:17:28 2026

@author: RAMYA KEERTHI
"""

import pandas as pd
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

## imported pandas for data analysis and matplotlib for visualization.

#pandas - used for data manipulation
#matplotlib - used for plotting charts

import os
os.chdir(r"D:\Data Analysr Training\My projects")
print(os.getcwd())

print(os.listdir())

df = pd.read_csv('employee_attrition_dataset.csv')

print("employee_attrition_dataset")
print(df)

df.head()

df.info()
df.describe()
###loaded the employee attrition dataset using pandas read_csv() function.
# This stores the dataset in a DataFrame called df.

df.isnull().sum()


#### Attrition Count
print(df['attrition'].value_counts())
##This function counts unique values in the attrition column.-- Helps understand overall employee turnover.

#### Attrition Percentage - Shows attrition rate in percentage form.

print(df['attrition'].value_counts(normalize = True)*100)
##calculated percentage of employees who left and stayed.
# - normalize=True gives proportion
# -multiplying by 100 converts to percentage

#### Attrition by Department

print(df[df['attrition']=='Yes'] ["department"].value_counts())
## filtered employees who left and counted them by department.
# Filters attrition = Yes,   Counts department-wise
# Identifies departments with high attrition.

#### Average Salary by Attrition

print(df.groupby('attrition')['salary'].mean())
## compared average salary between employees who left and stayed.
## groupby('attrition') splits data, mean() calculates average salary
#  Helps understand if salary impacts attrition.


#### Average Experience

print(df.groupby('attrition')['years_at_company'].mean())
## compared average years at company between employees who left and stayed.
## Shows whether new employees leave more.


### Performance Score Analysis
print(df.groupby('attrition')['performance_score'].mean())
# analyzed average performance scores for employees who left and stayed.
# Helps understand if performance is linked to attrition.

#### Attrition by Gender
print(df[df['attrition'] == 'Yes']['gender'].value_counts())
# analyzed attrition distribution across gender. Shows gender-wise attrition pattern.


#####  Attrition Rate by Department (%)

dept_attrition = df.groupby('department')['attrition'].value_counts(normalize=True).unstack() * 100
print(dept_attrition)

#### Attrition by Age Group  This helps in analyzing attrition across different age groups.
df["age_group"]= pd.cut(df['age'],
                      bins=[20,29,39,49,60],
                      labels=['20-29','30-39','40-49','50+'])

print(df["age_group"]);

print(df[df["attrition"] == "Yes"]["age_group"].value_counts())
# created a new column called age_group using pd.cut() to categorize employees into age ranges.
# pd.cut() divides continuous data into intervals
#bins define the ranges
#labels assign names to each range




#### EDA

# ATTRITION COUNT (BAR CHART)

df['attrition'].value_counts().plot(kind='bar')
plt.title('Attrition Count')
plt.xlabel('Attrition')
plt.ylabel('Number of Employees')
plt.show()
##  created a bar chart to show number of employees who left vs stayed.

#Insight:
## Quickly shows overall attrition distribution.


##### ATTRITION % (PIE CHART)

df['attrition'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Attrition Percentage')
plt.ylabel('')
plt.show()

#Attrition Percentage Visualization

###I created a pie chart to show percentage of employees who left.

## Insight:Helps understand attrition rate visually.


####ATTRITION BY DEPARTMENT - Visualized department-wise attrition.
# Identifies departments with high employee turnover.
df[df['attrition'] == 'Yes']['department'].value_counts().plot(kind='bar')
plt.title('Attrition by Department')
plt.xlabel('Department')
plt.ylabel('Attrition Count')
plt.show()


##### SALARY DISTRIBUTION -Used histogram to understand salary spread.
# Shows how salaries are distributed across employees.
df['salary'].plot(kind='hist', bins=10)
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.show()

#### EXPERIENCE VS ATTRITION - Compared average experience of employees who left vs stayed.
## Shows whether new employees are leaving more.
df.groupby('attrition')['years_at_company'].mean().plot(kind='bar')
plt.title('Average Experience by Attrition')
plt.ylabel('Years')
plt.show()


##### PERFORMANCE VS ATTRITION - Compared performance scores between employees.
## Checks if performance affects attrition.
df.groupby('attrition')['performance_score'].mean().plot(kind='bar')
plt.title('Performance Score by Attrition')
plt.ylabel('Score')
plt.show()


#### ATTRITION BY AGE GROUP -Visualized attrition across age categories.
# Shows which age group is leaving more.

df[df['attrition'] == 'Yes']['age_group'].value_counts().plot(kind='bar')
plt.title('Attrition by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.show()


#### Salary vs Attrition (Box Plot)

df.boxplot(column='salary', by='attrition')
plt.title('Salary vs Attrition')
plt.suptitle('')
plt.show()