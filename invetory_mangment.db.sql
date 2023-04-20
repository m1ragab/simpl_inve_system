BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Item" (
	"ItemID"	INT,
	"Name"	VARCHAR(255),
	"Price"	DECIMAL(10, 2),
	"main gatagory"	VARCHAR(255),
	"sub gatagory"	VARCHAR(255),
	'sub sub gatagory'	VARCHAR(255),
	PRIMARY KEY("ItemID")
);
CREATE TABLE IF NOT EXISTS "Inventory" (
    "InventoryID" INT,
	"Name" VARCHAR(255),
	"Location" VARCHAR(255),
    "ItemID" INT,
    "Quantity" INT,
    FOREIGN KEY("ItemID") REFERENCES "Item"("ItemID"),
    PRIMARY KEY("InventoryID")
);
CREATE TABLE IF NOT EXISTS "Transfer" (
	"TransferID"	INT,
	'Type'	VARCHAR(255), -- 'from-to' or 'to-from'
	"Date"	DATE,
	"Time"	TIME,
	"weight Quantity "	INT,
	"Quantity as number"	INT,
	"ItemID"	INT,
	"SourceInventoryID"	INT,
	"DestinationInventoryID"	INT,
	FOREIGN KEY("DestinationInventoryID") REFERENCES "Inventory"("InventoryID"),
	FOREIGN KEY("SourceInventoryID") REFERENCES "Inventory"("InventoryID"),
	FOREIGN KEY("ItemID") REFERENCES "Item"("ItemID"),
	PRIMARY KEY("TransferID")
);


CREATE TABLE IF NOT EXISTS "Manufacture" (
	"ManufactureID"	INT,
	"Date"	DATE,
	"Time"	TIME,
	"Quantity"	INT,
	"ProductID"	INT,
	"ComponentIDs"	VARCHAR(255),
	FOREIGN KEY("ProductID") REFERENCES "Item"("ItemID"),
	PRIMARY KEY("ManufactureID")
);
COMMIT;
