import sqlite3 as sql
import pandas as pd

def createDB():
    conn=sql.connect("carplates.db")
    conn.commit()
    conn.close()

def createTable():
    conn=sql.connect('carplates.db')
    cursor=conn.cursor()
    cursor.execute(
        '''CREATE TABLE plates3(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            PLATE TEXT,
            DATETIME TEXT
        )
        '''
    ) 

def insertrow(plt,dtt):
    conn=sql.connect('carplates.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO plates3 (PLATE,DATETIME) VALUES (?,?)', (plt,dtt))
    conn.commit()
    conn.close()

def deletetable():   
    conn=sql.connect("carplates.db")
    cursor=conn.cursor() 
    instruction=f"DROP TABLE plates2;"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def exportcv():
    conn=sql.connect("carplates.db")
    cursor=conn.cursor()
    instruction=f"SELECT * FROM plates3"
    cursor.execute(instruction)
    data=cursor.fetchall()
    conn.commit()
    conn.close()
    df = pd.DataFrame(data)
    df.to_csv (r'D:\csv.csv',index=False)

# def insertrow2(platee):
#     conn=sql.connect("carplates.db")
#     cursor=conn.cursor()
#     instruction=f"INSERT INTO plates2 VALUES ('{platee}')"
#     cursor.execute(instruction)
#     conn.commit()
#     conn.close()

# createDB()
# createTable()
# deletetable()
# insertrow('c','d')
# insertrow2(556)
