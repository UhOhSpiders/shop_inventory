import pdb
from db.run_sql import run_sql
from models.product import Product
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM products"
    results = run_sql(sql)

def save(product):
    sql = "INSERT INTO products (product_name, product_description, stock_quantity, merchant_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [product.product_name, product.product_description, product.stock_quantity, product.merchant.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        merchant = merchant_repository.select(row['merchant_id']) 
        product = Product(row['product_name'], row['product_description'], row['stock_quantity'], merchant, row['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        merchant = merchant_repository.select(result['merchant_id'])
        product = Product(result['product_name'], result['product_description'], result['stock_quantity'],merchant)
    return product

def update(product):
    sql = "UPDATE products SET (product_name, product_description, stock_quantity, merchant_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [product.product_name, product.product_description, product.stock_quantity, product.merchant.id, product.id]
    run_sql(sql, values)
