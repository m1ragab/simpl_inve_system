import unittest
import sqlite3
import os
from my_database import Database

class TestDatabase(unittest.TestCase):
    
    def test_create_tables(self):
        # Create a new database object
        database = Database("test_db.db")

        # Try to create the four tables
        try:
            database.create_tables()
        except Exception as sd:
            #raise error if the tables are not created successfully say hi
            self.fail(sd)
            

        # Check if the tables were created successfully
        with sqlite3.connect("test_db.db") as conn:
            cursor = conn.cursor()
            for table in ["Item", "Inventory", "Transfer", "Manufacture"]:
                cursor.execute("SELECT COUNT(*) FROM {}".format(table))
                self.assertEqual(cursor.fetchone()[0], 0)

    def test_table_exists(self):
        # Create a new database object
        database = Database("test_db.db")
        connection = sqlite3.connect("test_db.db")
        cursor = connection.cursor()

        # Check if the tables exist.
        tables = ["Item", "Inventory", "Transfer", "Manufacture"]
        for table in tables:
            result = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(table)).fetchone()
            if result is None:
                print("The table {} does not exist.".format(table))            
                assert result is not None 

        # Close the database connection.
        connection.close()
    # test insert value into table
    def test_insert_data(self):
        try:
            database = Database("test_db.db")
            database.insert_data('Item', [ 'Name', 'Price', 'main_category', 'sub_category', 'sub_sub_category'], ['test_item', 1.99, 'Fruit', 'Apple', 'Red Delicious'])
        except Exception as e:
            self.fail(e)
        with sqlite3.connect("test_db.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT Name FROM Item")
            self.assertEqual(cursor.fetchone()[0], "test_item")



if __name__ == "__main__":
    #remove the test_db.db before the test
    
    if os.path.exists("test_db.db"):
        os.remove("test_db.db")
    unittest.main()

