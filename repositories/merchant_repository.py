from db.run_sql import run_sql
from models.merchant import Merchant
import pdb

def save(merchant):
    sql = "INSERT INTO merchants (merchant_name, alignment) VALUES (%s, %s) RETURNING *"
    values = [merchant.merchant_name, merchant.alignment]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        merchant = Merchant(result['id'], result['merchant_name'], result['alignment'])
    return merchant

def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row['merchant_name'], row['alignment'], row['id'])
        merchants.append(merchant)
    return merchants

def delete_all():
    sql = "DELETE FROM merchants"
    results = run_sql(sql)


def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(merchant):
    sql = "UPDATE merchants SET (merchant_name, alignment) = (%s, %s) WHERE id = %s"
    values = [merchant.merchant_name, merchant.alignment, merchant.id]
    run_sql(sql, values)



