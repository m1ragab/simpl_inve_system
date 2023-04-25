"import database class from database.py"

from my_database import Database
db = Database('inv_data.db')
db.create_item_table()
db.cursor.execute("SELECT * FROM Item")
print(db.cursor.fetchall())

#insert data into tables
# Create a dictionary of data to insert.
data = {
    "Name": "Apple",
    "Price": 1.00,
    "main category": "Fruit",
    "sub category": "Red",
    "sub sub category": "Red Delicious"
}

# Insert the data into the Item table.
db.insert("Item", data)

db.commit()
db.cursor.execute("SELECT * FROM Item")
print(db.cursor.fetchall())
