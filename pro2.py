import numpy as np
import pandas as pd
data={
    'customer_id':[1,2,3,4,5,6,7,8,9,10],
    'customer_name':['John','Alice','Bob','Eve','Charlie','David','Frank','Grace','Hannah','Ivy'],
    'customer_age':[25,30,22,28,35,40,32,29,27,31],
    'customer_email':['john@example.com','alice@example.com','bob@example.com','eve@example.com','charlie@example.com','david@example.com','frank@example.com','grace@example.com','hannah@example.com','ivy@example.com']
}
df=pd.DataFrame(data)
print(df)
print("\nAverage Age:",df['customer_age'].mean())
print("Maximum Age:",df['customer_age'].max())
print("Minimum Age:",df['customer_age'].min())
print(df.describe())
print(df.groupby('customer_age')['customer_name'].count())
print("\nCustomers older than 30:")
older_customers=df[df['customer_age']>30]
print(older_customers)
print("\nCustomers sorted by age:")
sorted_customers=df.sort_values(by='customer_age',ascending=False)  
print(sorted_customers)
print("\nCustomers with age between 25 and 30:")
age_range_customers=df[(df['customer_age']>=25) & (df['customer_age']<=30)]
print(age_range_customers)
print("\nCustomers with email ending with 'example.com':")
example_email_customers=df[df['customer_email'].str.endswith('example.com')]    
print(example_email_customers)
print("\nCustomers with name starting with 'A':")
name_starting_A_customers=df[df['customer_name'].str.startswith('A')]
print(name_starting_A_customers)
print("\nCustomers with name containing 'a':")
name_containing_a_customers=df[df['customer_name'].str.contains('a',case=False)]
print(name_containing_a_customers)
print("\nCustomers with age greater than average age:")
average_age=df['customer_age'].mean()
print("Average Age:",average_age)
print(df[df['customer_age']>average_age])
print("\nCustomers with age less than average age:")
print(df[df['customer_age']<average_age])
print("\nCustomers with age equal to average age:")
print(df[df['customer_age']==average_age])
print("\nCustomers with age not equal to average age:") 
print(df[df['customer_age']!=average_age])
print("\nCustomers with age greater than or equal to average age:")
print(df[df['customer_age']>=average_age])
print([df['customer_email']])
print(df['customer_email'].isnull().sum())
print(df['customer_age'].sum())
print("\nCustomers with age greater than 30 and name starting with 'D':")
d_customers=df[(df['customer_age']>30) & (df['customer_name'].str.startswith('D'))]
print(d_customers)
print("\nCustomers with age less than 30 or name starting with 'E':")
e_customers=df[(df['customer_age']<30) | (df['customer_name'].str.startswith('E'))]
print(e_customers)
print("\nCustomers with age between 25 and 35 and name containing 'a':")
a_customers=df[(df['customer_age']>=25) & (df['customer_age']<=35) & (df['customer_name'].str.contains('a',case=False))]
print(a_customers)
print("\nCustomers with age not between 25 and 35 or name not containing 'a':")
not_a_customers=df[~((df['customer_age']>=25) & (df['customer_age']<=35) & (df['customer_name'].str.contains('a',case=False)))]
print(not_a_customers)
print(df[df['customer_name'].str.len()>4])
print(df)
print("\nCustomers with age greater than 30 and name starting with 'D':")
d_customers=df[(df['customer_age']>30) & (df['customer_name'].str.startswith('D'))]
print(d_customers)
print("\nCustomers with age greater than 30 and name starting with 'A':")
a_customers=df[(df['customer_age']>30) & (df['customer_name'].str.startswith('A'))]
print(a_customers)
print("\nCustomers with age greater than 30 and name starting with 'C':")
c_customers=df[(df['customer_age']>30) & (df['customer_name'].str.startswith('C'))]
print(c_customers) 
print(df[df['customer_name'].str.startswith('A') & (df['customer_age']>30)]) 
print(df[df['customer_name'].str.startswith('A') | (df['customer_age']>30)])
print(df[df['customer_name'].str.startswith('A') ^ (df['customer_age']>30)])
print(df[df['customer_email'].str.endswith('example.com')])
print(df[df['customer_email'].str.contains('example.com')])
print(df[df['customer_email'].str.match('.*@example.com')])