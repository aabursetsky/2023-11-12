"""
Домашнее задание по теме "Режимы открытия файлов"
"""


class Product:
    def __init__(self, name, weight, category):
        self.name = name                                        # название продукта
        self.weight = weight                                    # общий вес товара
        self.category = category                                # категория товара

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'
    if_file = open(__file_name, 'a')                            # создать пустой файл, если его нет
    if_file.close()

    def get_products(self):
        products = open(self.__file_name, 'r')
        list_products = products.read()
        products.close()
        return list_products

    def add(self, *products):
        for i in products:
            product_in_shop = self.get_products()
            if i.name in product_in_shop:
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                in_shop = open(self.__file_name, 'a')
                in_shop.write(f'{i}\n')
                in_shop.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

p4 = Product('Pasta', 5.5, 'Groceries')

s1.add(p4)

print(s1.get_products())
