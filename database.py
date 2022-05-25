import sqlite3

# Function for displaying Database(DB)
def show_all():
  conn=sqlite3.connect('customer.db')
  c=conn.cursor()
  c.execute("SELECT * from customers")
  items = c.fetchall()
  for item in items:
    print(item)
  conn.commit()
  conn.close()

# Function for adding new data in DB
def add_one(first,last,email):
  conn=sqlite3.connect('customer.db')
  c=conn.cursor()
  c.execute("INSERT INTO customers values(?,?,?)",(first,last,email))
  conn.commit()
  conn.close()

# Function for deleting data in DB
def delete_one(id):
  conn=sqlite3.connect('customer.db')
  c=conn.cursor()
  c.execute("DELETE from customers WHERE rowid = (?)",id)
  conn.commit()
  conn.close()

# Function for adding list of data in DB
def add_many(list):
  conn=sqlite3.connect('customer.db')
  c=conn.cursor()
  c.executemany("INSERT INTO customers values(?,?,?)",(list))
  conn.commit()
  conn.close()

# Function for looking data based on e_mail
def email_lookup(email):
  conn=sqlite3.connect('customer.db')
  c=conn.cursor()
  c.execute("SELECT  rowid, * from customers WHERE e_mail = (?)",(email,))
  items = c.fetchall()
  for item in items:
    print(item)
  conn.commit()
  conn.close()

