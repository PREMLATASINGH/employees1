import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data={
    'order_id':[101,102,103,104,105,106,107,108,109,110],
    'customer_id':[1,2,3,4,5,6,7,8,9,10],
    'order_amount':[250,300,150,400,350,200,450,500,600,700],
    'order_date':['2023-01-01','2023-01-02','2023-01-03','2023-01-04','2023-01-05','2023-01-06','2023-01-07','2023-01-08','2023-01-09','2023-01-10'],
    'order_status':['Completed','Pending','Completed','Cancelled','Completed','Pending','Completed','Completed','Cancelled','Completed']
,
'sales_region':['North','South','East','West','North','South','East','West','North','South'],
'product_category':['Electronics','Clothing','Home','Beauty','Electronics','Clothing','Home','Beauty','Electronics','Clothing'] ,
'price':[100,50,200,150,300,250,400,350,500,450],
'quantity':[2,3,1,4,2,5,3,2,1,4],
'discount':[10,5,20,15,30,25,40,35,50,45],
'tax':[5,2.5,10,7.5,15,12.5,20,17.5,25,22.5],
'payment_method':['Credit Card','PayPal','Credit Card','Debit Card','PayPal','Credit Card','Debit Card','PayPal','Credit Card','Debit Card'],
'delivery_time':[2,3,1,4,2,5,3,2,1,4],
'customer_feedback':['Good','Average','Excellent','Poor','Good','Average','Excellent','Poor','Good','Average'],
}
df=pd.DataFrame(data)
print(df)
print("\nAverage Order Amount:",df['order_amount'].mean())
print("Maximum Order Amount:",df['order_amount'].max())
print("Minimum Order Amount:",df['order_amount'].min())
print(df.describe())
print(df.columns)
print(df.info())
print(df['order_status'].value_counts())
print(df['sales_region'].value_counts())
print(df.isnull().sum())
print(df.groupby('sales_region')['order_amount'].mean())
print(df.groupby('product_category')['order_amount'].sum())
print(df.groupby('payment_method')['order_amount'].count())
print(df.groupby('customer_feedback')['order_amount'].mean())
print(df.groupby('order_status')['order_amount'].sum())
print(df.groupby('order_date')['order_amount'].median())
print(df.groupby('order_date').sum())
print(df.info())
print(df['customer_feedback'].value_counts())
print(df['product_category'].value_counts())
print(df['payment_method'].value_counts())
print(df['sales_region'].value_counts())
print(df['order_status'].value_counts())
print(df['order_date'].value_counts())
