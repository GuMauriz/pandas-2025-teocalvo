SELECT
    seller_id,
    SUM(price) AS valorVendas,
    COUNT(DISTINCT order_id) AS qtdVendas
FROM tb_order_items
GROUP BY 1;