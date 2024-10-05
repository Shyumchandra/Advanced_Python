import sqlite3 

conn=sqlite3.connect("sql.db")

cursor=conn.cursor()

cursor.execute("CREATE TABLE USERS (id INTEGER PRIMARY KEY,name TEXT)")
cursor.execute("INSERT INTO users (name) VALUEs ('ALICE')")
cursor.execute("SELECT * FROM users")

rows=cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()