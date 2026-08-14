import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data={
    'emp_id':[101,102,103,104,105,106,107,108,109,110],
    'emp_name':['John','Alice','Bob','Eve','Charlie','David','Frank','Grace','Hannah','Ivy'],
    'emp_salary':[50000,60000,55000,70000,65000,55000,60000,70000,55000,65000] , 
    'department':['HR','Finance','IT','Marketing','Sales','IT','Finance','HR','Marketing','Sales']  
}
df=pd.DataFrame(data)
print(df)
print("\nAverage Salary:",df['emp_salary'].mean())
print("Maximum Salary:",df['emp_salary'].max())
print("Minimum Salary:",df['emp_salary'].min())
print(df.describe()) 
print(df.groupby('department')['emp_salary'].mean()) 
print("\nEmployees with salary greater than 60000:")
high_salary_employees=df[df['emp_salary']>60000]  
print(high_salary_employees)
print("\nEmployees in IT department:")
it_department_employees=df[df['department']=='IT']  
print(it_department_employees)
print("\nEmployees sorted by salary:")
sorted_employees=df.sort_values(by='emp_salary',ascending=False)
print(sorted_employees)
print("\nEmployees with salary greater than 60000 in IT department:")
high_salary_it_employees=df[(df['emp_salary']>60000) & (df
['department']=='IT')]
print(high_salary_it_employees)
print("\nEmployees with salary greater than 60000 or in IT department:")
high_salary_or_it_employees=df[(df['emp_salary']>60000) | (df['department']=='IT')]
print(high_salary_or_it_employees)
print("\nEmployees with salary between 55000 and 65000:")
salary_range_employees=df[(df['emp_salary']>=55000) & (df['emp_salary']<=65000)]
print(salary_range_employees)
df2=pd.DataFrame({
    'emp_id':[111,112,113],     
    'emp_name':['Jack','Lily','Mia'],
    'emp_salary':[60000,70000,65000],
    'department':['HR','Finance','IT']
})
df_combined=pd.concat([df,df2],ignore_index=True)
print("\nCombined Employee Data:")
print(df_combined)
merged_df=pd.merge(df,df2,on='emp_id',how='outer',suffixes=('_left','_right'))
print("\nMerged Employee Data:")
print(merged_df)
print("\nEmployees with salary greater than 60000 after merging:")
high_salary_employees_merged=merged_df[merged_df['emp_salary_left']>60000]
print(high_salary_employees_merged)
print("\nEmployees in IT department after merging:")
it_department_employees_merged=merged_df[merged_df['department_left']=='IT']    
print(it_department_employees_merged)
print("\nEmployees sorted by salary after merging:")
sorted_employees_merged=merged_df.sort_values(by='emp_salary_left',ascending=False) 
print(sorted_employees_merged)
print("\nEmployees with salary greater than 60000 in IT department after merging:")
high_salary_it_employees_merged=merged_df[(merged_df['emp_salary_left']>60000) & (merged_df['department_left']=='IT')]
print(high_salary_it_employees_merged)
print("\nEmployees with salary greater than 60000 or in IT department after merging:")
high_salary_or_it_employees_merged=merged_df[(merged_df['emp_salary_left']>60000) | (merged_df['department_left']=='IT')]
print(high_salary_or_it_employees_merged)   
print("\nEmployees with salary between 55000 and 65000 after merging:")
salary_range_employees_merged=merged_df[(merged_df['emp_salary_left']>=55000) & (merged_df['emp_salary_left']<=65000)]
print(salary_range_employees_merged)
print("\nAverage Salary after merging:",merged_df['emp_salary_left'].mean())    
print("Maximum Salary after merging:",merged_df['emp_salary_left'].max())
print("Minimum Salary after merging:",merged_df['emp_salary_left'].min())
print(merged_df.describe())