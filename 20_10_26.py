import sqlite3
'''try:
    cursor.execute('UPDATE accounts SET balance=balance-1000 WHERE id=1')
    cursor.execute('UPDATE accounts SET balance=balance+1000 WHERE id=2')
    conn.commit()
exept:
    conn.rollback()'''

'''def create_db():
    conn=sqlite3.connect("accounts.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS people( id INTEGER PRIMARY KEY,name TEXT,balance INTEGER)")
    conn.commit()
    conn.close()

def insert_into():
    conn=sqlite3.connect("accounts.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO people(name,balance) VALUES ('Petya',2500)")
    conn.commit()
    conn.close()
#create_db()
#insert_into()
try:#изменение баланса
    conn=sqlite3.connect("accounts.db")
    cursor=conn.cursor()
    cursor.execute('UPDATE people SET balance=balance+1000 WHERE id=1')
    raise Exception("Power Failure")# выключение света==прерывание операции
    cursor.execute('UPDATE people SET balance=balance-1000 WHERE id=2')
    conn.commit()
    #conn.close()
except:
    conn.rollback()'''

'''from contextlib import closing
with closing(sqlite3.connect("database.db")) as conn:
    with conn:
        cursor=conn.cursor()
        cursor.execute("INSERT INTO..")'''

'''cursor.execute("SELECT id,name,email FROM users")
rows=cursor.fetchall()#запись в массив
users=[]
for row in rows:
    users.append(row[1])

conn.row_factory=sqlite3.Row
cursor=conn.cursor()
cursor.execute("SELECT id,name,email FROM users")
for row in cursor.fetchall():
    print(row['name'],row['email'])'''

'''def create_db():
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS games(id INTEGER PRIMARY KEY,user_id INTEGER,score INTEGER)")
    conn.commit()
    conn.close()

def insert_into():
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO games(user_id,score) VALUES (3,1000)")
    cursor.execute("INSERT INTO games(user_id,score) VALUES (3,2000)")
    cursor.execute("INSERT INTO games(user_id,score) VALUES (3,3000)")
    
    conn.commit()
    conn.close()
#create_db()
insert_into()'''

'''def create_db():
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)")
    conn.commit()
    conn.close()

def insert_into():
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO users(name,age) VALUES ('Kolya',20)")
    cursor.execute("INSERT INTO users(name,age) VALUES ('Petya',21)")
    cursor.execute("INSERT INTO users(name,age) VALUES ('Ivan',20)")
    cursor.execute("INSERT INTO users(name,age) VALUES ('Sergey',19)")
    conn.commit()
    conn.close()

create_db()
insert_into()'''
