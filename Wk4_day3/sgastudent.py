import sqlite3

conn = sqlite3.connect("sgastudent.db")

c = conn.cursor()
print("successful")

#practising altering of table in form of adding new column, changing table name 
#deleteing table

# c.execute(""" CREATE TABLE sga_lists(
#                     Name text,
#                     email text
#                 )

#             """)

# sga_list = [("Abubakar Adisa", "adisaabubakar@gmail.com"), ("Adebisi Afolabi" , "wasola.afolabi@yahoo.com"),("Adedoyin Abass", "doyinabass0@gmail.com"),
#                 ("Awonaike Tawakalitu", "purpleduralumin@gmail.com"),("Babajide Adesugba", "jide_ade@hotmail.com"),
#                 ("Bukola Ajayi", "bukolam.ajayi@gmail.com"), ("Binta Umar", "ubinta63@yahoo.com"),
#                 ("Christian Uzondu", "uzonduchristian2@gmail.com"), ("Cynthia Awiya", "awiyac@yahoo.com"),
#                 ("Deborah Olorunnishola", "deboraholuwatobi247@gmail.com"),("Eke Ihuoma", "ihuomaeke28@gmail.com"),
#                 ("Esther Akpanowo", "estherakpanowo@gmail.com"), ("Eniola Osadare", "dorcasosadare@gmail.com"), 
#                 ("Etariemi Louis", "etariemilouis@gmail.com")
#                 ]

# c.executemany("INSERT INTO sga_lists VALUES(?,?)", sga_list)

print("successful")

conn.commit()


Q= """SELECT *
        FROM sga_info"""

y = c.execute(Q)
z = c.fetchall()

print("Name" + "\t\tEmail" )
print("....." + "\t\t......")
for i in z:
    
    # Name, email = i
    print(i[0]+"\t\t" +i[1])

conn.commit()

#ALTER FUNCTIOn

# c.execute("ALTER TABLE sga_lists RENAME TO sga_info")
# conn.commit()
print("successful")

#ADDing more column
# c.execute("ALTER TABLE sga_info ADD COLUMN Track")

#Update Table
#adding info to the new colum added

c.execute("""UPDATE sga_info SET Track= 'Data Science' """)
# Qu= """SELECT *
#         FROM sga_info"""

# p = c.execute(Qu)
# r = c.fetchall()
# print(r)

#DElete Fucntion

c.execute("""DELETE FROM sga_info
                WHERE rowid='4'  """)

conn.commit()
print("successful")

Qu= """SELECT *
        FROM sga_info"""

p = c.execute(Qu)
r = c.fetchall()
print("Name" + "\t\tEmail" + "\t\tTrack" )
print("....." + "\t\t......")
for x in r:
    print(x[0] + "\t\t" + x[1]+ "\t\t" + x[2])


conn.commit()
conn.close()
