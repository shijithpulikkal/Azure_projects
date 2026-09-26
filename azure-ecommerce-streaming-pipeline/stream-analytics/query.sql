-- Raw event archive (unaggregated, for historical analysis later)
SELECT
    order_id,
    customer_state,
    product_category,
    quantity,
    unit_price,
    quantity * unit_price AS total_price,
    event_time
INTO blobArchive
FROM orderEvents

-- Live aggregated metrics for the Power BI dashboard
SELECT
    System.Timestamp() AS window_end,
    customer_state,
    product_category,
    COUNT(*) AS order_count,
    SUM(quantity * unit_price) AS revenue
INTO powerBiLive
FROM orderEvents
GROUP BY
    customer_state,
    product_category,
    TumblingWindow(second, 10)