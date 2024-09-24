import sqlite3

#Connect to the database
conn=sqlite3.connect('customer.db')

#Create a cursor
c=conn.cursor()

#Query The Database
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()
print(items)





print("Command executed successfully...")
#Commit our command
conn.commit()

#Close our connection
conn.close()

