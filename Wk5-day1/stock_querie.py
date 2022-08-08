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


q = """ SELECT *
        FROM Stock_item
        """

s = cursor.execute(q)
print("Item recorded in stationary shop")
for i in s:
        Id, Name, Qty, Cost = i
        
        print(f"{Id} \t\t {Name} \t\t {Qty} \t\t {Cost}")

print("\n Querie showing the items to restock i.e item with lowest quantity ")

def item_querie(column1, pattern):
        querie = f""" SELECT *
                FROM Stock_item
                ORDER BY {column1} {pattern}
                """

        y= cursor.execute(querie)
        for x in y:
                print(x)

print("\n Order of item from in ascending order. i.e lowest to highest quantity")
item_querie("Qty", "ASC")
print("According to this, the stationary shop need to restock Canvas first before other item ")

print("\n order of item according to their prices from higest to lowest price")
item_querie("cost", "DESC")


#commmit the database and the table
conn.commit()

#close the connection to the database
conn.close()


