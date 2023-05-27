-- Índices
-- Usado quando a tabela é mais usado para consultas

SELECT *
FROM PRODUCTS
WHERE CATEGORY_ID > 6;


CREATE INDEX IDX_CATEGORY ON PRODUCTS(CATEGORY_ID);