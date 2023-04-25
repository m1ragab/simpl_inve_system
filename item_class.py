import sqlite3
#import Database class from my_database.py
from my_database import Database
import tkinter as tk
from tkinter import messagebox

class Item:
    #class item for creting item objects from my_database.py
    def __init__(self,name,length,width,height,avg_weight,price,main_category,sub_category,sub_sub_category):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.avg_weight = avg_weight
        self.price = price
        self.main_category = main_category
        self.sub_category = sub_category
        self.sub_sub_category = sub_sub_category

    def check_item(self,db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            SELECT * FROM Item WHERE Name = ?;
        ''',(self.name,))
        result = self.cursor.fetchall()
        if result:
            return True
        else:
            return False
        
    #add item to database
    def add_item(self,db_name):
        print("Add item button clicked")  # Check if the method is being called
        #check if item exist frist
        if self.check_item(db_name):
            return print("Item already exist")

        else:
            self.connection = sqlite3.connect(db_name)
            self.cursor = self.connection.cursor()
            self.cursor.execute('''
                INSERT INTO Item (Name,length,Width,Height,Main_category,Sub_category,Sub_sub_category) VALUES (?,?,?,?,?,?,?);
            ''',(self.name,self.length,self.width,self.height,self.main_category,self.sub_category,self.sub_sub_category))
            self.connection.commit()
            self.connection.close()
            print("Item added")
        tk.messagebox.showinfo("Success", "Item added to database.")
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


