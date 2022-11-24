select s.customer_id ,C.age,I.item_name,sum(O.quantity)
from customers C left join sales s on c.customer_id=s.customer_id left join orders O on O.sales_id=s.sales_id left join items I on I.item_id=O.item_id 
where C.age<35 and C.age>18 and O.quantity not null 
group by s.customer_id,C.age,I.item_name;