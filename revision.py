#To create a database company with table project
import mysql.connector as db
con = db.connect(host='localhost', username='root', passwd='sql@123')
cur = con.cursor()

SQL = "CREATE DATABASE COMPANY;"
cur.execute(SQL)
SQL = "USE COMPANY;"
cur.execute(SQL)

SQL = "CREATE TABLE PROJECT(ProjectNo int, Title char(50), NOP int, Status char(50));"
cur.execute(SQL)
SQL = "INSERT INTO PROJECT VALUES(1,'project2',3,'in progress'), (2,'project2',2,'completed'), (3,'project3',4,'in progress');"
cur.execute(SQL)
con.commit

SQL = "UPDATE PROJECT SET NOP = NOP + 2 ;"
cur.execute(SQL)
con.commit()

cur.execute('select * from project')
r = cur.fetchall()
for no, title, num_per, stats in r:
    print( f"{no: <2}{title : ^20}{num_per: <2}{stats: ^20}")
con.close()