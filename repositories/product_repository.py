from db.run_sql import run_sql

def save(product):
    sql = "INSERT INTO products (product_name, product_description, stock_quantity, buying_cost, selling_cost, category, merchant_id, min_stock_level) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.product_name, product.product_description, product.stock_quantity, product.buying_cost, product.selling_cost, product.category, product.merchant_id, product.min_stock_level]
    id = results[0]['id']
    product.id = id
    return product