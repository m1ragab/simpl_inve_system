import tkinter as tk
import sqlite3
from tkinter import messagebox
from my_database import Database
from ss import Item

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Add Item")
        self.geometry("400x300")
        self.db_name = "asas.db"

        # Create the name label and entry.
        self.name_label = tk.Label(text="Name")
        self.name_entry = tk.Entry()

        # Create the category label and entry.
        self.category_label = tk.Label(text="Category")
        self.category_entry = tk.Entry()

        # Create the add button.
        self.add_button = tk.Button(text="Add", command=self.add_item_gui)
        #create the remove button
        self.remove_button = tk.Button(text="Remove", command=self.remove_item_gui)

        # Layout the widgets.
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.category_label.grid(row=1, column=0)
        self.category_entry.grid(row=1, column=1)
        self.add_button.grid(row=2, column=0, columnspan=2)
        self.remove_button.grid(row=3, column=0, columnspan=2)

    def add_item_gui(self):
        # Get the name and category from the user.
        name = self.name_entry.get()
        category = self.category_entry.get()


        # Create a new item object.
        item = Item(name, category)

        # Add the item to the database.
        item.add_item(self.db_name)

        # Print a message saying that the item was added to the database.
        print("Item added to the database")
        #remove item from database gui 
    def remove_item_gui(self):
        #get the name from the user
        name = self.name_entry.get()
        #get the category from the user
        category = ""
        #create a new item object
        item = Item(name,category)
        #remove item from database
        item.remove_item(self.db_name)
        #print a message saying that the item was removed from the database
        print("Item removed from the database")
        #remove item from database gui    


if __name__ == "__main__":
 #create item table using daTABASE CLASS
    app = App()
    app.mainloop()
    #print alll items in the database
    db = Database("asas.db")
    db.create_item_table()
    db.cursor.execute('''

        SELECT * FROM Item;

    ''')
    result = db.cursor.fetchall()
    print(result)

