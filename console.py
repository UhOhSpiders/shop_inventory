import pdb
from models.merchant import Merchant
from models.product import Product
import repositories.product_repository as product_repository
import repositories.merchant_repository as merchant_repository


# product_repository.delete_all()
# merchant_repository.delete_all()
merchant_1 = Merchant('Grogg', 'Chaotic Good')
merchant_repository.save(merchant_1)
# merchant_repository.delete(1)
# pdb.set_trace()
product_1 = Product('Lolipop', 'melted', 12, merchant_1)
product_2 = Product('Pocket Lint', 'useless', 12, merchant_1)
product_repository.save(product_1)
product_repository.save(product_2)
# merchant_repository.select(21)
result = product_repository.select(2)


