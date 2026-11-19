SELECT*FROM sales LIMIT 10;

SELECT count(*) AS total_rows FROM sales;

SELECT "Order ID", "Customer Name", sales
FROM sales
WHERE Sales>1000
ORDER BY Sales DESC;

SELECT "Order ID", City, sales
FROM sales
WHERE Region ='West' AND Category='Technology'
LIMIT 20;

SELECT Category, Round(SUM(Sales), 2) AS total_sales
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;

SELECT Region, Count(*) AS orders, round(AVG(Sales), 2) As avg_sale
FROM sales
GROUP BY Region;

SELECT "Product Name", round(SUM(Sales), 2) As total_sales
FROM sales
GROUP BY "Product Name"
ORDER BY total_sales DESC
LIMIT 10;

SELECT "Product Name", ROUND(SUM(Sales), 2) AS total_sales
From sales
GROUP BY "Product Name"
ORDER BY total_sales DESC
LIMIT 10;

SELECT Year, ROUND(SUM(Sales), 2) as total_sales
FROM sales
GROUP BY Year
ORDER BY Year;

SELECT State, ROUND(SUM(Sales), 2) AS total_sales
FROM sales
GROUP BY State
ORDER BY total_sales DESC
LIMIT 5;

SELECT Segment, COUNT(*) AS orders
FROM sales
GROUP BY Segment;