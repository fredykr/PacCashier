# PacCashier
Python Project Pacmann - Super Cashier

A. Background
Simple Cashier Invoice Program is a program to store purchased item into invoice or transaction. User can add, remove, update, view, reset as well as show grand total of item purchased.

B. Tools
- python
- git

C. Objective
User able to:
1. Create an invoice/transaction
2. Add item purchased into transaction
3. Update purchased item name to new name
4. Update purchased item quantity to new quantity
5. Update purchased item price to new price
6. Delete an purchased item
7. Reset all transaction become empty/blank
8. View all items purchased within a transaction
9. Show grand total of price

D. Program Description
1. main.ipynb   : main file as jupyter notebook format (will be converted to main.py in next version)
2. item.py      : parent class of item purchased
3. transaction.py   : child class inherit from item class, for storing transaction/invoice

E. Usage
1. Create transaction. Example: 
    transaction1 = Transaction()
2. Add item. Example: 
    transaction1.add_item(Item("mobil",1,1000))
3. Update item to new name. Example: 
    transaction1.update_item_name("mobil","truk")
4. Update item quantity. Example: 
    transaction1.update_item_quantity("truk",2)
5. Update item price. Example: 
    transaction1.update_item_price("truk","2000")
6. Delete item. Example: 
    transaction1.delete_item("truk")
7. Reset transaction. Example: 
    transaction1.reset_transaction()
8. View transaction. Example: 
    transaction1.check_order()
9. Show grand total. Example: 
    transaction1.total_price()

F. Next Release
1. Convert main.ipynb to main.py OR cashier.py
