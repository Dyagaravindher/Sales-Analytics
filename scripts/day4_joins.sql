DELETE FROM region_managers;

INSERT INTO region_managers VALUES
('West', 'Asha'), ('East', 'Dev'), ('Central', 'Mira'), ('South', 'Neel'), ('North', 'Zoya');

SELECT count(*) FROM region_managers;

SELECT m.Manager, s.Region, ROUND(SUM(s.Sales), 2) AS total_sales
FROM sales s
INNER JOIN region_managers m ON s.Region = m.Region
GROUP BY m.Manager, s.Region
ORDER BY total_sales DESC;

SELECT c.customer_name, c.Segment, ROUND(SUM(s.Sales), 2) AS total_sales
FROM sales s
JOIN customers c ON s."Customer ID" = c.customer_id
GROUP BY c.customer_id, c.customer_name, c.Segment
ORDER BY total_sales DESC
LIMIT 10;

SELECT COUNT(*) FROM region_managers;

SELECT m.Region, m.Manager, COUNT(s."Order ID") AS orders
FROM region_managers m
LEFT JOIN sales s ON m.Region = s.Region
GROUP BY m.Region, m.Manager;

SELECT m.Manager, s.Year, ROUND(SUM(s.Sales), 2) AS total_sales
FROM sales s
JOIN region_managers m ON s.Region = m.Region
GROUP BY m.Manager, s.Year
ORDER BY m.Manager, s.Year;

