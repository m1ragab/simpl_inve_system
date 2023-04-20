
class Item:
    def __init__(self, item_id, name, quantity, price, category):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    def delete_item(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("DELETE FROM Item WHERE ItemID = ?", (self.item_id,))
        conn.commit()
        conn.close()

    def get_transactions(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Transactions WHERE ItemID = ?", (self.item_id,))
        rows = c.fetchall()
        transactions = [Transaction(*row) for row in rows]
        conn.close()
        return transactions
    
    def get_total_value(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT SUM(Quantity) FROM Inventory WHERE ItemID = ?", (self.item_id,))
        row = c.fetchone()
        total_quantity = row[0] if row else 0
        total_value = total_quantity * self.price
        conn.close()
        return total_value
    def manufacture_item(self, component_ids, quantity):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        for component_id in component_ids:
            c.execute("UPDATE Inventory SET Quantity = Quantity - ? WHERE ItemID = ?", (quantity, component_id))
        c.execute("UPDATE Inventory SET Quantity = Quantity + ? WHERE ItemID = ?", (quantity, self.item_id))
        c.execute("INSERT INTO Manufacture (Date, Time, ProductID, ComponentIDs, Quantity) VALUES (?, ?, ?, ?, ?)", (date.today(), datetime.now().strftime("%H:%M:%S"), self.item_id, ','.join(map(str, component_ids)), quantity))
        conn.commit()
        conn.close()






class Inventory:
    def __init__(self, inventory_id, item_id, quantity):
        self.inventory_id = inventory_id
        self.item_id = item_id
        self.quantity = quantity

    @staticmethod
    def get_item_quantity(item_id, inventory_id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT Quantity FROM Inventory WHERE ItemID = ? AND InventoryID = ?", (item_id, inventory_id))
        row = c.fetchone()
        quantity = row[0] if row else 0
        conn.close()
        return quantity

    def add_to_inventory(self, quantity, inventory_id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("UPDATE Inventory SET Quantity = Quantity + ? WHERE ItemID = ? AND InventoryID = ?", (quantity, self.item_id, inventory_id))
        conn.commit()
        conn.close()

    def remove_from_inventory(self, quantity):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("UPDATE Inventory SET Quantity = Quantity - ? WHERE ItemID = ? AND InventoryID = ?", (quantity, self.item_id, self.inventory_id))
        conn.commit()
        conn.close()
       

       


class Transaction:
    def __init__(self, transaction_id, date, time, items):
        self.transaction_id = transaction_id
        self.date = date
        self.time = time
        self.items = items

    def record_transaction(self):
        # Code to record the transaction in the database
        pass

    def update_inventory(self):
        # Code to update the inventory based on the transaction
        pass


        def update_inventory(self):
    # Connect to the database
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    # Update the quantity of each item involved in the transaction
    for item in self.items:
        item_id = item['item_id']
        quantity = item['quantity']

        # Define the SQL query to update the quantity of the item
        query = """
            UPDATE Item
            SET Quantity = Quantity - ?
            WHERE ItemID = ?
        """

        # Execute the query with the values for the item
        c.execute(query, (quantity, item_id))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


class Transfer:
    # The __init__ method is a special method that is called when a new object is created
    # It takes the self parameter, which refers to the current object, and other parameters that are passed when creating the object
    # It assigns the values of the parameters to the attributes of the object
    def __init__(self, id, type, date, time, quantity, source_id, destination_id):
        self.id = id
        self.type = type
        self.date = date
        self.time = time
        self.quantity = quantity
        self.source_id = source_id
        self.destination_id = destination_id

    # The execute method is a custom method that performs the transfer by updating the source and destination inventories
    # It takes the self parameter and an inventory parameter, which is a list of Inventory objects
    # It finds the source and destination Inventory objects by matching their ids with the source_id and destination_id attributes of the Transfer object
    # It updates the quantity attribute of the source and destination Inventory objects by subtracting or adding the quantity attribute of the Transfer object, depending on the type attribute of the Transfer object
    # It prints a message indicating the result of the transfer
    def execute(self, inventory):
        # Find the source and destination Inventory objects in the inventory list
        source = None
        destination = None
        for inv in inventory:
            if inv.id == self.source_id:
                source = inv
            if inv.id == self.destination_id:
                destination = inv

        # Check if both source and destination are found
        if source and destination:
            # Check if the type of transfer is valid ('from-to' or 'to-from')
            if self.type == 'from-to':
                # Check if the source has enough quantity to transfer
                if source.quantity >= self.quantity:
                    # Update the quantity of source and destination by subtracting and adding respectively
                    source.quantity -= self.quantity
                    destination.quantity += self.quantity
                    # Print a success message
                    print(f"Transfer {self.id} executed successfully: {self.quantity} units of item {source.item_id} transferred from inventory {source.id} to inventory {destination.id}")
                else:
                    # Print an error message
                    print(f"Transfer {self.id} failed: insufficient quantity in inventory {source.id}")
            elif self.type == 'to-from':
                # Check if the destination has enough quantity to transfer
                if destination.quantity >= self.quantity:
                    # Update the quantity of source and destination by adding and subtracting respectively
                    source.quantity += self.quantity
                    destination.quantity -= self.quantity
                    # Print a success message
                    print(f"Transfer {self.id} executed successfully: {self.quantity} units of item {destination.item_id} transferred from inventory {destination.id} to inventory {source.id}")
                else:
                    # Print an error message
                    print(f"Transfer {self.id} failed: insufficient quantity in inventory {destination.id}")
            else:
                # Print an error message
                print(f"Transfer {self.id} failed: invalid type of transfer")
        else:
            # Print an error message
            print(f"Transfer {self.id} failed: source or destination inventory not found")
class Inventory:
    # The constructor method that initializes the attributes of the Inventory object
    def __init__(self, id, name, location, item_id, quantity):
        self.id = id
        self.name = name
        self.location = location
        self.item_id = item_id
        self.quantity = quantity
        # Get the Item object that corresponds to the item id
        self.item = self.get_item()
        # Set the price and category attributes from the Item object
        self.price = self.item.price
        self.category = self.item.category

    # The get_item method that returns the Item object that corresponds to the item id attribute of the Inventory object
    def get_item(self):
        # Find the Item object in the item list that matches the item id
        for item in item_list:
            if item.id == self.item_id:
                return item

    # The set_item method that sets the item id attribute of the Inventory object and updates the price and category attributes accordingly
    def set_item(self, new_item_id):
        # Set the new item id
        self.item_id = new_item_id
        # Get the new Item object that corresponds to the new item id
        self.item = self.get_item()
        # Set the new price and category attributes from the new Item object
        self.price = self.item.price
        self.category = self.item.category

    # The get_value method that returns the value of the inventory, which is the product of the quantity and price attributes of the Inventory object
    def get_value(self):
        return self.quantity * self.price

    # The display method that prints the information of the Inventory object in a formatted way
    def display(self):
        print(f"Inventory ID: {self.id}")
        print(f"Inventory Name: {self.name}")
        print(f"Inventory Location: {self.location}")
        print(f"Item ID: {self.item_id}")
        print(f"Item Name: {self.item.name}")
        print(f"Item Price: {self.price}")
        print(f"Item Category: {self.category}")
        print(f"Quantity: {self.quantity}")
        print(f"Value: {self.get_value()}")
