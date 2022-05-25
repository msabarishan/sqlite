import sqlite3
def show_all():
  conn=sqlite3.connect('customer.db')
  c=conn.cursor()
  c.execute("""CREATE TABLE customers (
          first_name text,
          last_name text,
          e_mail text )""")

  conn=sqlite3.connect('customer.db')
  c=conn.cursor()
  many_customers =[('Tom','Sawyer','tom@sawyer.com'),('Elon','Gates','elon@gates.com'),('Bill','Musk','bill@musk.com')]
  # Insert data into table
  c.executemany("INSERT INTO customers values(?,?,?)",many_customers)
  conn.commit()
  conn.close()

def add_one(first,last,email):
  conn=sqlite3.connect('customer.db')
  c=conn.cursor()
  c.execute("INSERT INTO customers values(?,?,?)",(first,last,email))
  conn.commit()
  conn.close()
