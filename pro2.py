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