import sqlite3
from tkinter import Y

conn = sqlite3.connect("WAEC_results.db")

cursor= conn.cursor()

print("Day 2 Assignment using the csv fle from database")
q = """ SELECT *
        FROM waec_r
    """

r= cursor.execute(q)

for i in r:
    Name, Maths, English, Physics, Biology, Economics, Commerce, Agric, Yoruba, French = i
    print(f"{Name}\t {Maths}\t{English}\t{Physics}\t {Biology} \t{Economics}\t {Commerce}\t {Agric}\t {Yoruba} \t{French}")


# #Queries based on assignment
#Note: question one and two can also be solved using max function, but i used the order by
#in that case, the select function will be "SELECT NAme, MAX(Maths)". in thiscase, ther is  no need for limit by

#he student with the higest csore in mathematics and english
def answer12(column1, column2, pattern):
    Querie = f"""SELECT {column1}
                FROM waec_r
                ORDER BY {column2} {pattern}
                LIMIT (1)
                """

    y = cursor.execute(Querie)
    for i in y:
        print(i)

print("\n The student with the higest csore in mathematics is: ")
answer12("Name", "Maths", "DESC")

print("\n The student with the lowest score in english is:")
answer12("Name", "English", "ASC")

#The average score of student in Maths and english

def answer34(columnp):
    querie = f"""SELECT AVG({columnp})
                    FROM waec_r
                
                    """

    Z = cursor.execute(querie)
    for x in Z:
            print(x)

print("\n The average score of student in Maths is")
answer34(("Maths"))

print("\nThe average score of student in English is")
answer34("English")


#he best performing student accross nine subject in terms of overall scores and average scores
def answer56(columnh, divisor, alias):
    querie3 = f"""SELECT {columnh},  (Maths+English+Physics+Biology+Economics+Commerce+Agric+Yoruba+French)/{divisor} AS {alias}
                        FROM waec_r
                        ORDER BY {alias} DESC
                        LIMIT(1)
                        """

    U = cursor.execute(querie3)
    for x in U:
                print(x)

print("\n The best performing student accross nine subject in terms of overall scores:")
answer56("Name", 1, "total_score")

print("\n The best performing student accross nine subject in terms of average scores:")
answer56("Name", 9, "Avg_score")




#please comment on my result if there is other way i can go about this. I have checked online but no simplify way
# Maths+English+Physics+Biology+Economics+Commerce+Agric+Yoruba+French            
conn.commit()

conn.close()