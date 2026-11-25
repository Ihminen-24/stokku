import sqlite3

DB_NAME = "stokku.db"

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    return conn

conn = connect_db()
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS products(product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    price REAL,
    stock INTEGER)""")
conn.commit()
conn.close()


cur.execute("""INSERT INTO products (product_name, price, stock)VALUES(?,?,?,?)""",(product_name,price,stock))
conn.commit()
conn.close()
