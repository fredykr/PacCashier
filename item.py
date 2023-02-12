from dataclasses import dataclass

#@dataclass
class Item():
    def __init__(self, name, qty, price):
        self.Name = name
        self.Qty = qty
        self.Price = price
        self.Total = qty * price
        self.Enable = 1