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


Python Database Connection:
# ===========================
Ex: How to Give connection for any Database in Python?
# ======================================================

Standard Steps for any Database:
# ================================
For MYSQL Databse:
# ------------------
Step 1: myssql.connector.connect()
Step 2: conn.cursor()
Step 3: cursor.execute()
Step 4: conn.commit()
Step 5: cursor.close() and conn.close()