# # import mysql.connector

# # database = mysql.connector.connect(
# #     host = "localhost",
# #     user = "root",
# #     password = "Mydatabase82#@"
# # )

# # mycursor = database.cursor()
# # mycursor.execute("create database if not exists bookstore")
# # mycursor.execute("use bookstore")
# # mycursor.execute("""
# #                 CREATE TABLE IF NOT EXISTS books (
# #                     id INT AUTO_INCREMENT PRIMARY KEY,
# #                     title VARCHAR(50), 
# #                     author VARCHAR(50)
# #                 );
# # """)
# # mycursor.execute("""
# # INSERT INTO books (title, author)
# # VALUES (%s, %s);
# # """, ("Things fall apart", "chinue"))
# # database.commit()

# import mysql.connector

# # Connect to MySQL server (using hardcoded credentials)
# database = mysql.connector.connect(
#     host="localhost",
#     user="new_user",
#     password="newuserpassword"
# )

# mycursor = database.cursor()

# # Create and select the bookstore database
# mycursor.execute("CREATE DATABASE IF NOT EXISTS bookstores")
# mycursor.execute("USE bookstores")

# mycursor.execute("""
#     CREATE TABLE IF NOT EXISTS books (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         title VARCHAR(50),
#         author VARCHAR(50)
#     );
# """)

# mycursor.execute("""
#     INSERT INTO books (title, author)
#     VALUES (%s, %s);
# """, ("Things Fall Apart", "Chinua Achebe"))

# # Commit the changes
# database.commit()

# mycursor.execute("select * from books")
# result = mycursor.fetchall()
# for row in result:
#     print(row)


import mysql.connector

# Connect to MySQL server (using hardcoded credentials)

mydb = mysql.connector.connect(
    host="localhost",
    user="new_user",
    password="newuserpassword"
)


mycursor = mydb.cursor()

# Create the database and table if they don't exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS bookstores;")
mycursor.execute("USE bookstores;")
mycursor.execute(
    """CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(100) NOT NULL
    );"""
)

# Function to add a new book
# def add_book(title, author):
#     sql = "INSERT INTO books (title, author) VALUES (%s, %s)"
#     values = (title, author)
#     mycursor.execute(sql, values)
#     mydb.commit()
#     print("Book added successfully!")
# add_book("hello", "hi")
# mycursor.execute("select * from books")
# result = mycursor.fetchall()
# for row in result:
#     print(row)

# Function to view all books
# def view_books():
#     mycursor.execute("SELECT * FROM books")
#     result = mycursor.fetchall()
#     print("\n--- All Books ---")
#     for row in result:
#         print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}")
        
# view_books()

# Function to update a book's title and author
# def update_book(book_id, new_title, new_author):
#     sql = "UPDATE books SET title = %s, author = %s WHERE id = %s"
#     values = (new_title, new_author, book_id)
#     mycursor.execute(sql, values)
#     mydb.commit()
#     print("Book updated successfully!")

# update_book(2,"my new book", "bob")

def delete_book(book_id):
    sql = "DELETE FROM books WHERE id = %s"
    mycursor.execute(sql, (book_id,))
    mydb.commit()
    print("Book deleted successfully!")

delete_book(4)

mycursor.execute("select * from books")
result = mycursor.fetchall()
for row in result:
    print(row)

# # Function to delete a book by ID
# def delete_book(book_id):
#     sql = "DELETE FROM books WHERE id = %s"
#     mycursor.execute(sql, (book_id,))
#     mydb.commit()
#     print("Book deleted successfully!")


# # Close the connection when done
# mycursor.close()
# mydb.close()
# print("Database connection closed.")



