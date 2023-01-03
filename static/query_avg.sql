select  ITEMS.item_number, ITEMS.ordering_day, ITEMS.delivery_day, ITEMS.suggested_retail_price as sales_prices_suggestion,
ITEMS.profit_margin, ITEMS.purchase_price, ITEMS.item_categories, ITEMS.extra_categories, ITEMS.tags, ITEMS.case_content_quantity, ITEMS.case_content_unit,
(SALES.sales_quantity - INVENTORY.inventory) / ITEMS.case_content_quantity as QUANTITY_TO_ORDER,
	avg(SALES.sales_quantity) as average_sales,
	SALES.day AS SALES_DAY,
	INVENTORY.day as INVENTORY_DAY,
	INVENTORY.inventory AS INVENTORY_QUANTITY
from sales_predictions SALES
left JOIN inventory INVENTORY
	ON INVENTORY.item_number = SALES.item_number
	AND INVENTORY.day = SALES.day
JOIN (select * from orderable_items UNION select * from item_orders) as ITEMS
ON INVENTORY.item_number = ITEMS.item_number
group by SALES.item_number, SALES.day
HAVING  avg(SALES.sales_quantity) > INVENTORY.inventory