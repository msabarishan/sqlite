import database

# if table does not exist in database use the following codes else skip to line 7
database.create_table("customers")

# Adding list of data into Database DB)
data_list =[
    ('Brenda','Smart','brenda@smart.com'),
    ('Ezhikil','Kingston','ezhikil@kingston.com'),
    ('Leonard','Cooper','leonard@cooper.com')
    ]
database.add_many(data_list)

# Displaying the data from DB
database.show_all()

# Lookup and display based on e_mail address
database.email_lookup("brenda@smart.com")

# Deleting data from database based on ID
database.delete_one('5')

