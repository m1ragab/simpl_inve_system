"import database class from database.py"
from my_database import Database
db = Database('my_database.db')
db.create_tables()
"import Item class from main_file.py"

from main_file import Item


db = Database('my_database.db')
item = Item(db, 'Item 1', 9.99, 'Category 1', 'Subcategory 1', 'Subsubcategory 1')
item.creat_item()
item = Item(db, 'Item 2', 19.99, 'Category 1', 'Subcategory 1', 'Subsubcategory 2')
item.creat_item()
item = Item(db, 'Item 3', 29.99, 'Category 1', 'Subcategory 2', 'Subsubcategory 1')
item.creat_item()
item = Item(db, 'Item 4', 39.99, 'Category 1', 'Subcategory 2', 'Subsubcategory 2') 
item.creat_item()
item = Item(db, 'Item 5', 49.99, 'Category 2', 'Subcategory 1', 'Subsubcategory 1')
"print all items in the database"
db.cursor.execute('''
    SELECT * FROM Item
''')
print(db.cursor.fetchall())


