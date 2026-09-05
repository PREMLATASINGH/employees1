import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data ={
    'employee_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'employee_name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie', 'David', 'Frank', 'Grace', 'Hannah', 'Ivy'],
    'department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales', 'HR', 'Finance', 'IT', 'Marketing', 'Sales'],
    'salary': [50000, 60000, 55000, 70000       , 65000, 52000, 58000, 62000, 72000, 68000],
    'hire_date': ['2020-01-15', '2019-03-10', '2021-06-20', '2018-11-05', '2020-09-30', '2019-12-01', '2021-02-14', '2018-07-25', '2020-05-18', '2019-08-22'],
    'performance_score': [4.5, 4.2, 4.8, 4.0, 4.3, 4.6, 4.1, 4.7, 4.4, 4.9],
    'bonus': [5000, 6000, 5500, 7000        , 6500, 5200, 5800, 6200, 7200, 6800]   

}
df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.describe())
print(df.info())
print(df['salary'].mean())
print(df['salary'].median())
print(df['salary'].std())
print(df['salary'].min())
print(df.isnull().sum())
print(df['department'].value_counts())
print(df.groupby('department')['salary'].mean())
print(df.sort_values('salary', ascending=False))
print(df.sort_values('salary', ascending=True))
print(df.groupby('department').size())