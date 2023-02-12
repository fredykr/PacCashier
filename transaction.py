from dataclasses import dataclass
#from item import *
import item

#@dataclass
class Transaction():   
    grandtotal: float = 0
    counter: int = 0

    def __init__(self):
        self.Item = []

    def add_item(self, item_name):
        self.counter+=1
        self.Item.append(item_name)
        #self.items.item['total'] = item_qty * self.items.item['price']
        #grandtotal = item.total
        return (self)

    def update_item_name(self, item_name, new_item_name):
        for t in self.Item:
            if t.Name == item_name and t.Enable == 1:
                t.Name = new_item_name
            else:
                continue

    def update_item_quantity(self, item_name, new_item_qty):
        for t in self.Item:
            if t.Name == item_name and t.Enable == 1:
                t.Qty = new_item_qty
                t.Total = new_item_qty * t.Price
            else:
                continue

    def update_item_price(self, item_name, new_item_price):
        for t in self.Item:
            if t.Name == item_name and t.Enable == 1:
                t.Price = new_item_price
                t.Total = new_item_price * t.Qty
            else:
                continue

    def delete_item(self, item_name):
        for t in self.Item:
            if t.Name == item_name and t.Enable == 1:
                t.Enable = 0
                #del self
                #del t
            else:
                continue

    def reset_transaction(self):
        for t in self.Item: t.Enable = 0

    def check_order(self):
        i = 0
        print(f'| No | Nama Item | Jumlah Item | Harga/Item | Total Harga |')
        print(f'|----|-----------|-------------|------------|-------------|')
        for t in self.Item: 
            if t.Enable == 1:
                i+=1
                print(f'| {i}  | {t.Name}     | {t.Qty}           | {t.Price}       | {t.Total}        |')

    def total_price(self):
        for t in self.Item:
            if t.Enable == 1:
                self.grandtotal += t.Total
        return self.grandtotal

    def __iter__(self):
        return iter(self.Item)
