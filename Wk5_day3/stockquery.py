import sqlite3


conn = sqlite3.connect("stocks.db")
#check that the connection is succesful
print("Database created successfully", type(conn))

#create a cusor object that allows the execution of SQL statement
cursor = conn.cursor()
print("cursosr created successfully", type(cursor))

print("Item recorded in stationary shop")

que1 = """ 
        SELECT  *
                FROM Stock_item
                """

A =  cursor.execute(que1)       
for i in A:
        Id, Name, Qty, Cost = i
        
        print(f"{Id} \t\t {Name} \t\t {Qty} \t\t {Cost}")

#The amount the owner investd in the procurement of the item and average quamtity in stock

def ans1(pattern, column1):
    que2 = f""" 
            SELECT  {pattern}({column1})
                    FROM Stock_item
                    """

    B = cursor.execute(que2)
    for p in B:
                    print(p)

print("\n The amount the owner investd in the procurement of the item")
ans1("SUM", "COST*Qty")

print("\n Averae quantity of item in stock")
ans1("AVG", "Qty")

# Item with the least and most quantity in stock
def ans2(columnp, columnq, pattern1):
    que3 = f""" 
                SELECT {columnp}, {columnq}
                        FROM Stock_item
                        Order BY Qty {pattern1}
                        LIMIT (1)
                        """

    C = cursor.execute(que3)
    p= cursor.fetchall()
    print(p)

print("\n Item with the least quantity in stock")
ans2("Name", "Qty", "ASC")

print("\n Item with the most quantity in stock")
ans2("Name", "Qty", "DESC")