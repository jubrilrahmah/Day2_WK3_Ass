# from curses import ACS_GEQUAL
from distutils.util import execute
import sqlite3

from colorama import Cursor

#connect or create to a database "i.e stock databse= stock.db"
conn = sqlite3.connect("stocks.db")
#check that the connection is succesful
print("Database created successfully", type(conn))

#create a cusor object that allows the execution of SQL statement
cursor = conn.cursor()

#verify that the cusor is created successfully
print("cursosr created successfully", type(cursor))


Stock_item = """ CREATE TABLE IF NOT EXISTS Stock_item(
                        Id INTEGER, 
                        Name TEXT,
                        Qty INTEGER,
                        Cost INTEGER
                )  
        """

cursor.execute(Stock_item)

Stock_item = [(1003, "Canvas", 20, 600), (1007, "Marker", 50, 100),
                (1023, "Pencil", 100, 50), (1006, "Books", 30, 200),
                (1009, "Eraser", 35, 70), (1016, "Blades", 34, 20),
                (1024, "Envelop", 22, 150), (1015, "Crayon", 45, 60),
                (1020, "Ruler", 60, 10), (1022,"sharpener", 85, 5)
]

cursor.executemany(""" INSERT INTO Stock_item VALUES(?,?,?,?)""", Stock_item)

print("\n Stock items recorded is: ", cursor.rowcount)

print("Item recorded in stationary shop")
for i in Stock_item:
        Id, Name, Qty, Cost = i
        
        print(f"{Id} \t\t {Name} \t\t {Qty} \t\t {Cost}")

print("\n Querie showing the items to restock i.e item with lowest quantity ")




#commmit the database and the table
conn.commit()

#close the connection to the database
conn.close()


