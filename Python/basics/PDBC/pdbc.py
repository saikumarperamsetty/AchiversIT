# Database Connection in Python:
# =============================
# --> It means of establishing communication between a software component and a database to enable interaction.

# Two types of storage system:
# ============================
# 1. temporary: 
# ------------
# --> list, tuple, set and dictonary.

# 2. persistent: 
# ------------
# --> file, database, data warehouses, Big data technologies etc....

# Database key Features:
# =====================
# 1. Data Management.
# 2. Data Integrity.
# 3. Data Retrieval:
# 4. Concurrency control:
# 5. Security:
# 6. Backup and Recovery:
# 7. Support for application:
# 8. Analysis and Reporting:
# 9. Reduced Data redundancy:
# 10. Versatile:
# 11. Scalable:


# Python Database Connection:
# ===========================
# Ex: How to Give connection for any Database in Python?
# ======================================================

# Standard Steps for any Database:
# ================================
# For MYSQL Databse:
# ------------------
# Step 1: myssql.connector.connect()
# Step 2: conn.cursor()
# Step 3: cursor.execute()
# Step 4: conn.commit()
# Step 5: cursor.close() and conn.close()

# sqlite3 Database:
# =================
# Ex: How to Write Queries in sqlite3 Database?
# import sqlite3
# connection = sqlite3.connect('sqlite3.db')

# cursor = connection.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)''')

# cursor.execute('''INSERT INTO users(name,age) VALUES(?,?) ''',('SAI',28))
# cursor.execute('''INSERT INTO users(name,age) VALUES(?,?) ''',('NTR',41))

# connection.commit()

# cursor.execute('''SELECT * FROM users''')

# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# connection.close()



# Python - MySQL Database connection:
# ===================================
# Ex: How to Give connection for Python - MySQL Database in Python?
# =================================================================
# First istall MySQL environment on your Python.
# pip install mysql-connector-python

# import mysql.connector
# from config import DB_CONFIG
# connection = mysql.connector.connect(
#     host = DB_CONFIG["host"],
#     user = DB_CONFIG['user'],
#     password = DB_CONFIG['host'],
#     database = DB_CONFIG['dbconnection']
# )
# cursor = connection.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)''')

# cursor.execute('''
# INSERT INTO users(name,age) VALUES(%s,%s)''',('Alice',30))
# cursor.execute('''
# INSERT INTO users(name,age) VALUES(%s,%s)''',('Bob',27))

# connection.commit()

# cursor.execute('''
# SELECT * FROM users''')

# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# connection.close()



# Ex: Realtime Example for Python - MySQL Database for CRUD Operations?
import mysql.connector
from config1 import DB_CONFIG1

connection = mysql.connector.connect(

    host = DB_CONFIG1['localhost'],
    user = DB_CONFIG1['root'],
    password = DB_CONFIG1['root'],
    database = DB_CONFIG1['dbconnection']
    
)

cursor = connection.cursor()

# CREATE QUERY
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees(
               id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(50),
               jobrole VARCHAR(50),
               salary DECIMAL(10,2)
               )
''')

# INSERT QUERY
insert_query = 'INSERT INTO employees(name,jobrole,salry) VALUES(%s,%s,%s)'
execute_insert_data = ('SAI KUMAR','Python Developer',80000)
cursor.execute(insert_query,execute_insert_data)

# UPDATE QUERY
update_query_data = 'UPDATE employees SET salary = %s WHERE name = "SAI KUMAR"'
cursor.execute(update_query_data,(90000,'SAI KUMAR'))

# DELETE QUERY
delete_query_data = 'DELETE FROM employees WHERE name = %s'
cursor.execute(delete_query_data,('SAI KUMAR',))

connection.commit()

cursor.execute('SELECT * FROM employees')

rows = cursor.fetchAll()
for row in rows:
    print(row)

connection.close()