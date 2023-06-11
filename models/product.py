class Product:

    def __init__(self, product_name, product_description, stock_quantity, buying_cost, selling_cost, category,min_stock_level, merchant, id = None):
        self.product_name = product_name
        self.product_description = product_description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_cost = selling_cost
        self.category = category
        self.min_stock_level = min_stock_level
        self.merchant = merchant
        self.id = id 