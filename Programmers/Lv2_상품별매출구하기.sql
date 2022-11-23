SELECT PRODUCT_CODE, sum(SALES_AMOUNT * PRICE) AS SALES
FROM PRODUCT
natural join Offline_sale
group by product_code
order by SALES desc, product_code