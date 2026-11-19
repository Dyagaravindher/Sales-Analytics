SELECT "Sub-Category", round(Sum(Sales), 2) AS total_sales
FROM sales
HAVING SUM(Sales)>100000
ORDER BY total_sales DESC;

SELECT "Customer Name", count(DISTINCT "Order ID") As orders
FROM sales
GROUP BY "Customer ID", "Customer Name"
HAVING count(DISTINCT "Order ID")>=10
ORDER BY orders DESC
LIMIT 10;

SELECT "Customer Name", count(DISTINCT "Order ID") AS orders
FROM sales
GROUP BY "Customer ID", "Customer Name"
HAVING COUNT (DISTINCT "Order ID")>=10
ORDER BY orders DESC
LIMIT 10;

SELECT State, ROUND(SUM(Sales), 2) AS total_sales
FROM sales
WHERE Year = 2018
GROUP BY State
HAVING SUM(Sales) > 20000
ORDER BY total_sales DESC;

SELECT strftime('%Y-%m', "Order Date") AS Month, 
		round(SUM(Sales), 2) AS total_sales
FROM sales
GROUP BY Month
ORDER BY Month;

SELECT Year,
		(CAST(strftime('%m', "Order Date") AS INTEGER)+2)/3 AS quarter,
		ROUND(SUM(Sales), 2) AS total_sales
FROM sales
GROUP BY Year, quarter
ORDER BY Year, quarter;


SELECT "Ship Mode",
			ROUND(AVG(julianday("Ship Date") - julianday("Order Date")), 1) AS avg_days_to_ship
From sales
GROUP BY "Ship Mode";


