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
