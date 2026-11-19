CREATE TABLE IF NOT EXISTS customers AS
SELECT DISTINCT "Customer ID" AS customer_id, "Customer Name" AS customer_name, Segment
FROM sales;

SELECT COUNT(*) FROM customers;

CREATE TABLE IF NOT EXISTS region_managers (Region TEXT, Manager TEXT);
