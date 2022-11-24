import sqlite3
import pandas as pd

conn=sqlite3.connect('test.db')
c=conn.cursor()
sql_query=pd.read_sql_query('''select s.customer_id as CUSTOMER ,C.age as AGE,I.item_name AS ITEM,sum(O.quantity) as Quantity from customers C left join sales s on c.customer_id=s.customer_id left join orders O on O.sales_id=s.sales_id left join items I on I.item_id=O.item_id where C.age<35 and C.age>18 and O.quantity not null group by s.customer_id,C.age,I.item_name;''',conn)

df=pd.DataFrame(sql_query)
print(df)
df.to_csv('AssesmentPythonSolution.csv',index=False,sep=';')
