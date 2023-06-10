class Product:

    def __init__(self, product_name, product_description, stock_quantity, merchant, id = None):
        self.product_name = product_name
        self.product_description = product_description
        self.stock_quantity = stock_quantity
        self.merchant = merchant
        self.id = id