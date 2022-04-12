import sqlite3
conn = sqlite3.connect('customerdb.db')

#create a cursor
c = conn.cursor()

#create table
c.execute("""CREATE TABLE customers (
    firstn text,
    lastn text,
    email text
)""")
#null(non-existent), integer(whole num), real(decimal), text, blob(image, mp3, etc.)

#commit our command
conn.commit()

#close conn just in case
conn.close()






