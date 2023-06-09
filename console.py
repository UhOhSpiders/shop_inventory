import pdb
from models.merchant import Merchant
import repositories.product_repository as product_repository
import repositories.merchant_repository as merchant_repository

# merchant_repository.delete_all()
merchant_1 = Merchant('Grogg', 'Chaotic Good')
merchant_repository.save(merchant_1)
print(merchant_repository.select(7))
product_1 = Product('Lolipop', 'melted', 12, 110, 120, 'misc', )
