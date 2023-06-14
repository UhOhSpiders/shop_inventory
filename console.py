import pdb
from models.merchant import Merchant
from models.product import Product
import repositories.product_repository as product_repository
import repositories.merchant_repository as merchant_repository

product_repository.delete_all()
merchant_repository.delete_all()
merchant_1 = Merchant('Grogg', 'Chaotic', 'Good', 'groggy@gmail.com')
merchant_2 = Merchant('Careful Whisperer', 'Neutral', 'Evil', 'carefulfeet@gmail.com')
merchant_3 = Merchant('Buff Humanoid Squirell', 'Lawful', 'Good', 'jeff@nutty.com')
merchant_4 = Merchant('John Smith', 'Neutral', 'Neutral', 'john.smith1@gmail.com')
merchant_5 = Merchant('Goblin Brewing Co.', 'Lawful', 'Good', 'sales@gbc.com')
merchant_6 = Merchant('David Cameron With The Head of a Praying Mantis', 'Lawful', 'Evil', 'daveydave@gmail.com')

product_1 = Product('Lolipop', 'melted', 12, 1, 1.50, 'vegetable', 10, merchant_1)
product_2 = Product('Pocket Lint', 'useless', 5, 0.50, 0.70, 'vegetable', 10, merchant_1)
product_3 = Product('Empty Crisp Packets', 'still some crumbs', 2, 1, 1.20, 'mineral', 10, merchant_1)
product_4 = Product('Mysterious Glowing Orb', 'screams when you touch it', 1, 100, 200, 'mineral', 10, merchant_2)
product_5 = Product('200 sheets of A4 paper', 'decent quality', 50, 2, 4.50, 'mineral', 10, merchant_4)
product_6 = Product('20 pack of biros', 'black ink', 20, 5, 8, 'mineral', 10, merchant_4)
product_7 = Product('Massive Acorns', 'takes 2 goblins to lift them', 6, 10, 25, 'vegetable', 10, merchant_3)
product_8 = Product('Haunted Toaster', 'burns satantic messages into every slice', 1, 70, 199.99, 'mineral', 10, merchant_2)
product_9 = Product('Vial of Human Tears', 'too salty', 17, 20, 50, 'animal', 10, merchant_6)
product_10 = Product('Wizard Beard IPA', 'tastes greate once you pick the hairs out', 24, 3, 5, 'vegetable', 10, merchant_5)
product_11= Product('Forgotten Pickaxe Stout', 'do not sell any more of this to Grogg', 24, 2, 4, 'vegetable', 10, merchant_5)

merchant_repository.save(merchant_1)
merchant_repository.save(merchant_2)
merchant_repository.save(merchant_3)
merchant_repository.save(merchant_4)
merchant_repository.save(merchant_5)
merchant_repository.save(merchant_6)

product_repository.save(product_1)
product_repository.save(product_4)
product_repository.save(product_5)
product_repository.save(product_6)
product_repository.save(product_7)
product_repository.save(product_8)
product_repository.save(product_9)
product_repository.save(product_2)
product_repository.save(product_3)
product_repository.save(product_10)
product_repository.save(product_11)
