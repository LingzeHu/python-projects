import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='' user='' password='' host='localhost' port='' ")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='' user='' password='' host='localhost' port='' ")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" %(item, quantity, price))
    # it can also be
    # cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='' user='' password='' host='localhost' port='' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM  store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

create_table()
# insert("Coffee Glass", 10, 5)
# insert("Wine Glass", 10, 5)
# insert("Purified Water", 10, 5)
# print(view())
# delete("Coffee Glass")
# update("Purified Water", 100, 50)
# print(view())
