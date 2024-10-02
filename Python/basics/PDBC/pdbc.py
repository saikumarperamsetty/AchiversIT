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
import sqlite3
connection = sqlite3.connect('sqlite3.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)''')

cursor.execute('''INSERT INTO users(name,age) VALUES(?,?) ''',('SAI',28))
cursor.execute('''INSERT INTO users(name,age) VALUES(?,?) ''',('NTR',41))

connection.commit()

cursor.execute('''SELECT * FROM users''')

rows = cursor.fetchall()
for row in rows:
    print(row)
    
connection.close()