import sqlite3
import csv

conn = sqlite3.connect("WAEC_results.db")
#check that the connection is succesful
print("Database created successfully", type(conn))

#create a cusor object that allows the execution of SQL statement
cursor = conn.cursor()
print("cursosr created successfully", type(cursor))
print("connecting the csv file to datbase for assignment")

Results = """ CREATE TABLE  waec_r (
            Name TEXT,
            Maths INTEGER,
            English INTEGER,
            Physics INTEGER,
            Biology INTEGER,
            Economics INTEGER,
            Commerce INTEGER,
            Agric INTEGER,
            Yoruba INTEGER,
            French INTEGER
            )    
    """

cursor.execute(Results)


#open the CVS file and read it using the csv module
with open("Waec_score.csv") as myfile:
    read_file = csv.reader(myfile)

    #skip header
    #The below code denote that the file print the data without the header 
    next(read_file)
    #inssert values of the read file into the SQL table
    cursor.executemany(""" INSERT INTO waec_r VALUES (?,?,?,?,?,?,?,?,?,?)""", read_file)

    y = """SELECT *
            FROM waec_r"""

    z = cursor.execute(y)

    for i in z:
        print(i)

print("executed succesfully")

conn.commit()

conn.close