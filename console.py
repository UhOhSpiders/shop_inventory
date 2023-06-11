import pdb
from models.merchant import Merchant
from models.product import Product
import repositories.product_repository as product_repository
import repositories.merchant_repository as merchant_repository


product_repository.delete_all()
merchant_repository.delete_all()
merchant_1 = Merchant('Grogg', 'Chaotic', 'Good')
merchant_repository.save(merchant_1)
product_1 = Product('Lolipop', 'melted', 12, 10, 12, 'misc', 10, merchant_1)
product_2 = Product('Pocket Lint', 'useless', 12, 2, 2, 'misc', 10, merchant_1)
product_repository.save(product_1)
product_repository.save(product_2)
# merchant_repository.select(21)
# result = product_repository.select(2)
# result_2 = product_repository.select_all()
# result_3 = merchant_repository.select_all()
merchant_1.morals = 'Evil'
# merchant_repository.select(23)
merchant_repository.update(merchant_1)
# merchant_repository.save(merchant_1)
product_2.product_description = 'very tasty'
product_repository.update(product_2)

print(product_1.merchant.merchant_name)