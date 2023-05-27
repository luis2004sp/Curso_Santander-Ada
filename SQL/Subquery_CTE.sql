--select *
--from order_details as O
--where O.quantity > (
--		-- Subquery
--		select avg(O.quantity)
--		from order_details as O
--		)
--order by O.quantity	


-- CTE => Common  Table Expressinon
with average as(
		select avg(O.quantity) as average_quantity
		from order_details as O
)

select * 
from order_details, average
where quantity > average.average_quantity
