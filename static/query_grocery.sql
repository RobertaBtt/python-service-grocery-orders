
SELECT
    DISTINCT
    orderable_items.item_number,
    orderable_items.ordering_day AS ordering_day,
    orderable_items.delivery_day AS delivery_day,	
	orderable_items.suggested_retail_price AS sales_price_suggestion,
	orderable_items.profit_margin AS profit_margin,
	orderable_items.purchase_price AS purchase_price,
	orderable_items.item_categories AS item_categories,
	orderable_items.extra_categories AS extra_categories,
	orderable_items.tags AS labels,
	orderable_items.case_content_quantity AS case_quantity,
	orderable_items.case_content_unit AS case_unit,
	ceil((sales_predictions.sales_quantity - inventory.inventory) / orderable_items.case_content_quantity) AS order_quantity,
	'CS' AS order_unit,
	inventory.inventory AS inventory_quantity
	
FROM orderable_items
   LEFT JOIN inventory
   ON orderable_items.item_number = inventory.item_number
   AND DATE(inventory.day) = ordering_day
     LEFT JOIN order_intake
     ON orderable_items.item_number = order_intake.item_number
     AND DATE(order_intake.day) = delivery_day
	LEFT JOIN sales_predictions
	ON orderable_items.item_number = sales_predictions.item_number
	AND DATE(sales_predictions.day) = delivery_day;

