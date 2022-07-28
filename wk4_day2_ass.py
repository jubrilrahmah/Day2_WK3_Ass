from distutils.util import execute
import sqlite3

from colorama import Cursor

#connect or create to a database "i.e student databse= student.db"
conn = sqlite3.connect("student.db")

#check that the connection is succesful
print("Database created successfully", type(conn))

#create a cusor object that allows the execution of SQL statement
cursor = conn.cursor()

#verify that the cusor is created successfully
print("cursosr created successfully", type(cursor))

#creating a table that consist of list of student in Data science track.
student_list = """
                CREATE TABLE IF NOT EXISTS student_list(
                    first_name text,
                    last_name text,
                    email text
                )
        """
cursor.execute(student_list)

student_list = [("Abubakar", "Adisa", "adisaabubakar@gmail.com"), ("Adebisi", "Afolabi" , "wasola.afolabi@yahoo.com"),("Adedoyin", "Abass", "doyinabass0@gmail.com"),
                ("Awonaike", "Tawakalitu", "purpleduralumin@gmail.com"),("Babajide", "Adesugba", "jide_ade@hotmail.com"),
                ("Bukola", "Ajayi", "bukolam.ajayi@gmail.com"), ("Binta", "Umar", "ubinta63@yahoo.com"),
                ("Christian", "Uzondu", "uzonduchristian2@gmail.com"), ("Cynthia", "Awiya", "awiyac@yahoo.com"),
                ("Deborah", "Olorunnishola", "deboraholuwatobi247@gmail.com"),("Eke", "Ihuoma", "ihuomaeke28@gmail.com"),
                ("Esther", "Akpanowo", "estherakpanowo@gmail.com"), ("Eniola", "Osadare", "dorcasosadare@gmail.com"), 
                ("Etariemi", "Louis", "etariemilouis@gmail.com"), ("Faith", "Amure", "amuretalodabif@gmail.com"),
                ("Ganiyat", "Shittu", "ganiyatas@gmail.com"),("Gideon", "Uko", "ukogideon13@gmail.com"),
                ("Idowu", 'Adesanya', 'idsworld22@yahoo.com'),("Joyce", "Ezeonwu", "joyceokore@gmail.com"),
                ("Kehinde", "Orolade", "kehindeorolade@gmail.com"), ("Kafayat", "Ibrahim", "kafayatadenike10@gmail.com"),
                ("Lawrence", "Aneshimokha", "anelawrence1@gmail.com"), ("Mariam", "Adeoti", "adetutuadebola28@gmail.com"),
                ("Ogechi", "Njemanze", "ogenjemz@gmail.com"), ("Omowunmi", "Awonirana", "mowunmi11@gmail.com"),
                ("Placidus", "Ali", "Placidusali@gmail.com"), ("Praise", "Emmanuel", "praiseemmanuel9ic@gmail.com"),
                ("Prince", "Ekeocha", "prince.ekeocha@gmail.com"), ("Rasheedat", "Sikiru", "rasheedatsikiru@gmail.com"),
                ("Ramotallah", "Jubril", "jubrilramotallah03@gmail.com"), ("Sheriiff", "Azeez", "SheriffOlaitan71@gmail.com"),
                ("Stephen", "Ogungbile", "stephenfunso@gmail.com"), ("Temitope", "Bamidele", "bamideletemitope42@gmail.com"),
                ("Theresa", "Karamor", "teriekarie@gmail.com"), ("Tina", "Uyateide", "tinauyats@gmail.com"), 
                ("Victoria", "Chukwuno" , "chukwunovictoria@gmail.com")
                ]

cursor.executemany(
    """INSERT INTO student_list  VALUES (?, ?, ? )
    """,
    student_list)

print("The no of rows in the table: ", cursor.rowcount)
print("Table excecuted successfully")

cursor.execute("""SELECT * From student_list""")
#Before the use of fetchmany, the table intend to fetch from must have been selected. 
itemss = cursor.fetchmany(10)
print(itemss)

# check that the table is executed succesfully


#commmit the database and the table
conn.commit()

#close the connection to the database
conn.close()
