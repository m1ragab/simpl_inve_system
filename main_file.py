import sqlite3

class Item:
    def __init__(self, db, name, price, main_category, sub_category, sub_sub_category):
        self.db = db
        self.name = name
        self.price = price
        self.main_category = main_category
        self.sub_category = sub_category
        self.sub_sub_category = sub_sub_category

    def creat_item(self):
        if not self.item_exists():
            self.db.cursor.execute('''
                INSERT INTO Item (Name, Price, "main gatagory", "sub gatagory", "sub sub gatagory")
                VALUES (?, ?, ?, ?, ?)
            ''', (self.name, self.price, self.main_category, self.sub_category, self.sub_sub_category))
            self.db.conn.commit()
        
    
    def item_exists(self):
        self.db.cursor.execute('''
            SELECT * FROM Item
            WHERE Name = ? AND Price = ? AND "main gatagory" = ? AND "sub gatagory" = ? AND "sub sub gatagory" = ?
        ''', (self.name, self.price, self.main_category, self.sub_category, self.sub_sub_category))
        return self.db.cursor.fetchone() is not None
    



