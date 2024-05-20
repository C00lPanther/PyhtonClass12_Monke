#To create an python connect sql server for management of a store

import mysql.connector as sql_con
con = sql_con.connect(host="localhost", username="root", password="pessword", database="stationary")
cur=con.cursor()

def AddItem():
    Ino = input("Ino :")
    IName = input("Name :")
    Qty = input("Qty :")
    Price = input("Price :")
    Dot = input("Date(YYYY-MM-DD)")
    Trans = "D"
    SQL = "INSERT INTO ISTOCK VALUES ({},'{}',{},{},'{}','{}')".format(Ino,IName,Qty,Price,Dot,Trans)
    
    cur.execute(SQL)
    con.commit()
    SQL = "SELECT count(*) FROM ISTOCK"
    cur.execute(SQL)
    R = cur.fetchall()
    print( R , "Items in stock " )


def ViewItems():
    SQL = "SELECT * FROM ISTOCK"
    cur.execute (SQL)
    R = cur.fetchall()
    for ino,name,price,qty,dot,tr in R :
        print("%4d|%20s|%5d|%8.2f|%12s|%2s"%(ino,name.ljust(20," "),price,qty,dot,tr))

def SearchItem():
    Ino = input('Ino')
    SQL = "SELECT * FROM ISTOCK WHERE Ino = {} ".format(Ino)
    cur.execute(SQL)
    R = cur.fetchone()
    if int(R[0])==int(Ino):
        print('Found .......')
        print('Ino :',R[0])
        print('Item :',R[1])
        print('Price :',R[2])
        print('Quantity :',R[3])
        print('Last transaction done on :',R[4])
        Stats = "Purchase" if R[5]=="P" else "Sale"
        print('Last transaction :',Stats)
    
def BuyItem():
    Ino = input('Ino')
    SQL = "SELECT count(*) FROM ISTOCK WHERE INO = {}".format(Ino)
    cur.execute(SQL)
    R = cur.fetchone()[0]
    if R>0:
        Qty = input("Qty bought")
        DOT = input("Date[YYYY-MM-DD]")
        Trans = "B"
        SQL = "UPDATE ISTOCK SET Qty=Qty+{} , DOT='{}', TRANS='{}' WHERE Ino={}".format(Qty,DOT,Trans,Ino)
        cur.execute(SQL)
        con.commit()
        



