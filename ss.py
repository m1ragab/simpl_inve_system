import sqlite3
from tkinter import messagebox
from my_database import Database
class Item:
    def __init__(self, name, main_category):
        self.name = name
        self.main_category = main_category
    
    def check_item(self, db_name):
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Item WHERE Name = ?', (self.name,))
        result = cursor.fetchall()
        connection.close()
        if result:
            return True
        else:
            return False
        
    def add_item(self, db_name):
        if self.check_item(db_name):
            print("Item already exists")
        else:
            connection = sqlite3.connect(db_name)
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Item (Name, Main_category) VALUES (?, ?)', (self.name, self.main_category))
            connection.commit()
            connection.close()
            print("Item added to the database")
    def remove_item(self,db_name):
        #check if item exist frist
        if self.check_item(db_name):
            pass
        else:
            return print("Item does not exist")
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            DELETE FROM Item WHERE Name = ?;
        ''',(self.name,))
        self.connection.commit()
        self.connection.close()
        print("Item removed")

# creat item table using daTABASE CLASS
# db = Database("my_database.db")
# db.create_item_table()

# item = Iatem("Apple", "Fruit")

# # add the item to the database
# item.add_item("my_database.db")
