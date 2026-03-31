-- Write your query below
select c.name 
from customers c
where c.id not in 
(select o.customer_id from orders o group by 1 );