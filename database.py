import sqlite3

db = sqlite3.connect('users.db')
try:
    conn = db.cursor()
    conn.execute(''' CREATE TABLE login(
        ID INTIGER PRIMARY KEY AUTOINCREMENT,
        username TEXT (15) NOT NULL,
        pin INTEGER,
        ); ''')
    print('Table created successfully')
except:
    print('Error: Operation Not Successful')
    db.rollback()
db.close()
