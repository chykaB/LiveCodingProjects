# import mysql.connector

# database = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "Mydatabase82#@"
# )

# mycursor = database.cursor()
# mycursor.execute("create database if not exists bookstore")
# mycursor.execute("use bookstore")
# mycursor.execute("""
#                 CREATE TABLE IF NOT EXISTS books (
#                     id INT AUTO_INCREMENT PRIMARY KEY,
#                     title VARCHAR(50), 
#                     author VARCHAR(50)
#                 );
# """)
# mycursor.execute("""
# INSERT INTO books (title, author)
# VALUES (%s, %s);
# """, ("Things fall apart", "chinue"))
# database.commit()

import mysql.connector

# Connect to MySQL server (using hardcoded credentials)
database = mysql.connector.connect(
    host="localhost",
    user="new_user",
    password="newuserpassword"
)

mycursor = database.cursor()

# Create and select the bookstore database
mycursor.execute("CREATE DATABASE IF NOT EXISTS bookstores")
mycursor.execute("USE bookstores")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(50),
        author VARCHAR(50)
    );
""")

mycursor.execute("""
    INSERT INTO books (title, author)
    VALUES (%s, %s);
""", ("Things Fall Apart", "Chinua Achebe"))

# Commit the changes
database.commit()

mycursor.execute("select * from books")
result = mycursor.fetchall()
for row in result:
    print(row)