import sqlite3
import pandas as pd

conn=sqlite3.connect('test.db')
c=conn.cursor()
sql_query1=pd.read_sql_query('''select * from customers''',conn)
sql_query2=pd.read_sql_query('''select * from orders''',conn)
sql_query3=pd.read_sql_query('''select * from Items''',conn)
sql_query4=pd.read_sql_query('''select * from Sales''',conn)


df_customers=pd.DataFrame(sql_query1)
df_order=pd.DataFrame(sql_query2)
df_sales=pd.DataFrame(sql_query4)
df_items=pd.DataFrame(sql_query3)

frames=df_customers.merge(df_sales)
frames1=frames.merge(df_order)
main_df=frames1.merge(df_items)

main_df=main_df[main_df['age']<35] 
main_df=main_df[main_df['age']>18]
main_df=main_df[main_df['quantity'].notnull()]
main_df=main_df[['customer_id','age','item_name','quantity']]
a=main_df.groupby(['customer_id','age','item_name'])['quantity'].sum()
a.to_csv('pythonsolution.csv',sep=';')
print(a)










