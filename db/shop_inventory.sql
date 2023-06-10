DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS merchants;

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    merchant_name VARCHAR(255),
    alignment VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    product_description VARCHAR (255),
    stock_quantity INT,
    merchant_id INT NOT NULL REFERENCES merchants(id)
);

    -- buying_cost INT,
    -- selling_cost INT,
    -- category VARCHAR(255),
    -- min_stock_level INT

-- INSERT INTO merchants (merchant_name, alignment) VALUES ('ganglebert', 'lawful good');
-- INSERT INTO products (product_name, product_description, stock_quantity, buying_cost, selling_cost, category, merchant_id, min_stock_level) VALUES
-- ('Hogweed', 'Smells bad', '12', '1', '15', 'ingredient', '1','15');