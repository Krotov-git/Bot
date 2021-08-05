import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS media_db")
cursor.execute("""CREATE TABLE IF NOT EXISTS media_db
                   (id int,
                    file_id REAL,
                    file_name TEXT);
                   """)
# test = [('3455343', '71', '91')]
#
# query = "INSERT into media_db values (?, ?, ?)"
# cursor.executemany(query, test)

connection.commit()

with connection:
     cursor = connection.cursor()
     cursor.execute("SELECT * FROM media_db")

     while True:
         row = cursor.fetchone()
         if row == None:
             break
         print(row[0], row[1], row[2])
