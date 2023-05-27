-- Window functions - Usada para analizes especificas 
-- Podem ser de:
-- Ranqueamento
-- Agregação (sum , max, mim, avg, ...)
-- Posição

-- Qual a primeira venda e qual foi o produto dela que um funcionario vendou?
select distinct 
	   employee_id,
	   first_value (order_date) over (partition by employee_id order by order_date) as first_date ,
	   first_value (product_name) over (partition by employee_id order by order_date) as first_product   
from orders
inner join order_details on 
orders.order_id = order_details.order_id
inner join products on
products.product_id = order_details.product_id
