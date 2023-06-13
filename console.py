import pdb
from models.merchant import Merchant
from models.product import Product
import repositories.product_repository as product_repository
import repositories.merchant_repository as merchant_repository


product_repository.delete_all()
merchant_repository.delete_all()
merchant_1 = Merchant('Grogg', 'Chaotic', 'Good', 'grogg@gmail.com')
merchant_repository.save(merchant_1)
product_1 = Product('Lolipop', 'melted', 12.50, 10, 12, 'animal', 10, merchant_1)
product_2 = Product('Pocket Lint', 'useless', 12.32, 2, 2, 'mineral', 10, merchant_1)
product_3 = Product('Lolipop', 'melted', 12.50, 10, 12, 'animal', 10, merchant_1)
product_4 = Product('Pocket Lint', 'useless', 12.32, 2, 2, 'mineral', 10, merchant_1)
product_5 = Product('Lolipop', 'melted', 12.50, 10, 12, 'animal', 10, merchant_1)
product_6 = Product('Pocket Lint', 'useless', 12.32, 2, 2, 'mineral', 10, merchant_1)
product_7 = Product('Lolipop', 'melted', 12.50, 10, 12, 'animal', 10, merchant_1)
product_8 = Product('Pocket Lint', 'useless', 12.32, 2, 2, 'mineral', 10, merchant_1)
product_9 = Product('Lolipop', 'melted', 12.50, 10, 12, 'animal', 10, merchant_1)
product_10 = Product('Pocket Lint', 'useless', 12.32, 2, 2, 'mineral', 10, merchant_1)
product_11= Product('Lolipop', 'melted', 12.50, 10, 12, 'animal', 10, merchant_1)
product_12= Product('Pocket Lint', 'useless', 12.32, 2, 2, 'mineral', 10, merchant_1)


product_repository.save(product_1)
product_repository.save(product_2)
product_repository.save(product_3)
product_repository.save(product_4)
product_repository.save(product_5)
product_repository.save(product_6)
product_repository.save(product_7)
product_repository.save(product_8)
product_repository.save(product_9)
product_repository.save(product_10)
product_repository.save(product_11)
product_repository.save(product_12)
# merchant_repository.select(21)
# result = product_repository.select(2)
# result_2 = product_repository.select_all()
# result_3 = merchant_repository.select_all()
merchant_1.morals = 'Evil'
# merchant_repository.select(23)
merchant_repository.update(merchant_1)
# merchant_repository.save(merchant_1)
print(product_2.product_description)
product_2.product_description = 'very tasty'
product_repository.update(product_2)

result = product_repository.select(product_2.id)
catergory_test = (product_repository.select_by_category('misc'))
print(catergory_test)
print(product_1.merchant.merchant_name)
print(product_1.category)
print(result.product_description)
print(product_2.product_description)