CREATE OR ALTER VIEW dbo.vw_curated_sales AS
SELECT *
FROM OPENROWSET(
    BULK ''https://stecommercedlspl.blob.core.windows.net/curated/*.parquet'',
    FORMAT = ''PARQUET''
) AS rows;
GO

SELECT TOP 100 *
FROM dbo.vw_curated_sales;
