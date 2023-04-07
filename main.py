class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, other):
        if isinstance(other, ShopItem):
            return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash((self.name.lower(), str(self.weight), str(self.price)))

lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']

shop_items = {}
for item in lst_in:
    name, weight, price = item.rsplit(maxsplit=2)
    obj = ShopItem(name[:-1], weight, price)
    shop_items.setdefault(obj, [obj, 0])[1] += 1