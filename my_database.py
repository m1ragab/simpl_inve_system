import sqlite3
import os
class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        
        self.cursor = self.connection.cursor()

    def create_item_table(self):
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS "Item" (
                    "ItemID" INTEGER PRIMARY KEY AUTOINCREMENT ,
                    "Name" VARCHAR(255),
                    "main_category" VARCHAR(255)
                );
            ''')
##TODO  "avg_Price" DECIMAL(10, 2),
##TODO  "الوزن القايم" DECIMAL(10, 2),
##TODO  "الوزن الصافي" DECIMAL(10, 2),
##TODO  "avg_weight" INT,

    def create_inventory_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS "Inventory" (
                "InventoryID" INT,
                "inventory_name" VARCHAR(255),
                "Location" VARCHAR(255),
                "ItemID" INT,
                "Quantity" INT,
                PRIMARY KEY("InventoryID")
            );
        ''')

    def create_transfer_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS "Transfer" (
                "TransferID" INT,
                'Type' VARCHAR(255), -- 'from-to' or 'to-from'
                "Date" DATE,
                "Time" TIME,
                "weight Quantity " INT,
                "Quantity as number" INT,
                "ItemID" INT,
                "SourceInventoryID" INT,
                "DestinationInventoryID" INT,
                FOREIGN KEY("DestinationInventoryID") REFERENCES "Inventory"("InventoryID"),
                FOREIGN KEY("SourceInventoryID") REFERENCES "Inventory"("InventoryID"),
                FOREIGN KEY("ItemID") REFERENCES "Item"("ItemID"),
                PRIMARY KEY("TransferID")
            );
        ''')

    def create_manufacture_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS "Manufacture" (
                "ManufactureID" INT,
                "Date" DATE,
                "Time" TIME,
                "Quantity" INT,
                "ProductID" INT,
                PRIMARY KEY("ManufactureID")
            );
        ''')

    def create_tables(self):
        self.create_item_table()
        self.create_inventory_table()
        self.create_transfer_table()
        self.create_manufacture_table()
    def commit(self):
        self.connection.commit()
    def closing(self):
        self.connection.close()
    def table_exists(self, table_name):
        """Checks if the specified table exists in the database.

        Args:
            table_name (str): The name of the table to check.

        Returns:
            bool: True if the table exists, False otherwise.
        """

        # Check if the table exists.
        sql = "SELECT EXISTS (SELECT 1 FROM sqlite_master WHERE type='table' AND name='{}')".format(table_name)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()[0]
        return result
    def insert_data(self, table_name, column_names, values):
        """Inserts data into a table.

        Args:
            table_name: The name of the table.
            column_names: A list of column names.
            values: A list of values.

        Returns:
            The number of rows inserted.
        """

        sql_statement = 'INSERT INTO {} ({}) VALUES ({})'.format(
            table_name, ','.join(column_names), ','.join('?' * len(column_names))
        )

        self.cursor.execute(sql_statement, values)
        self.connection.commit()
        return self.cursor.rowcount
    

#creat all tables


#insert data into the table
# Path: main.py
# Database('my_database.db').insert_data('Item', [ 'Name', 'Price', 'main_category', 'sub_category', 'sub_sub_category'], ['Apple', 1.99, 'Fruit', 'Apple', 'Red Delicious'])

