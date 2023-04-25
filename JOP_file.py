from my_database import Database
#import item class from ss.py
from ss import Item

#create item table using daTABASE CLASS
db = Database("aas.db")
db.create_item_table()
#creat Iatem object
item = Item("Apple", "Fruit")
#add item to the database
item.add_item("aas.db")



#print alll items in the database
db.cursor.execute('''
    SELECT * FROM Item;
''')

result = db.cursor.fetchall()

