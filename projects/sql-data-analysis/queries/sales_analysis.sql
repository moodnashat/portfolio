-- Sales Analysis SQL Portfolio Project
-- Source: projects/excel-sales-analysis/data/sales_data.csv

-- 1. Total sales
SELECT SUM(Sales) AS total_sales
FROM sales;

-- 2. Total orders and quantity
SELECT COUNT(DISTINCT Order_ID) AS total_orders,
       SUM(Quantity) AS total_quantity
FROM sales;

-- 3. Sales by region
SELECT Region,
       SUM(Sales) AS total_sales
FROM sales
GROUP BY Region
ORDER BY total_sales DESC;

-- 4. Sales by category
SELECT Category,
       SUM(Sales) AS total_sales
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;

-- 5. Top products by revenue
SELECT Product,
       SUM(Sales) AS total_sales
FROM sales
GROUP BY Product
ORDER BY total_sales DESC;

-- 6. Monthly sales
SELECT EXTRACT(MONTH FROM Order_Date) AS sales_month,
       SUM(Sales) AS total_sales
FROM sales
GROUP BY EXTRACT(MONTH FROM Order_Date)
ORDER BY sales_month;

-- 7. Average order value
SELECT AVG(Sales) AS average_order_value
FROM sales;
