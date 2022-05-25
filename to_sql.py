import database

# if table does not exist in database use the following codes else skip
# Codes for creating table named 'customers
conn=sqlite3.connect('customer.db')
c=conn.cursor()
c.execute("""CREATE TABLE customers (
          first_name text,
          last_name text,
          e_mail text )""")
conn.commit()
conn.close()

# Adding list of data into Database table (DBT)
data_list =[
    ('Brenda','Smart','brenda@smart.com'),
    ('Ezhikil','Kingston','ezhikil@kingston.com'),
    ('Leonard','Cooper','leonard@cooper.com')
    ]
database.add_many(data_list)

# Displaying the data from DBT
database.show_all()

# Lookup and display based on e_mail address
database.email_lookup("brenda@smart.com")

# Deleting data from DBT based on ID
database.delete_one('5')

# OTHERS
# To delete table
conn=sqlite3.connect('customer.db')
c=conn.cursor()
c.execute("DROP TABLE customers")
conn.commit()
conn.close()

# Limit and order by
conn=sqlite3.connect('customer.db')
c=conn.cursor()
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")
items =c.fetchall()
for item in items:
    print(item)
conn.commit()
conn.close()

# And OR
conn=sqlite3.connect('customer.db')
c=conn.cursor()
c.execute("SELECT * FROM customers WHERE last_name LIKE 'S%' OR first_name LIKE 'R%' OR e_mail LIKE 't%'")
items =c.fetchall()
for item in items:
    print(item)
conn.commit()
conn.close()

# Update existing records
conn=sqlite3.connect('customer.db')
c=conn.cursor()
c.execute("""UPDATE customers SET first_name ='George'
           WHERE last_name='Wood'""")
conn.commit()
conn.close()
