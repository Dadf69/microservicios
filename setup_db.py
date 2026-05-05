import mysql.connector

# Connect to MySQL (assuming root with no password)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

# Create database if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS biblioteca")

# Use the database
cursor.execute("USE biblioteca")

# Read and execute the SQL file
with open("biblioteca.sql", "r", encoding="utf-8") as f:
    sql = f.read()

# Split by ; and execute each statement
statements = sql.split(";")
for stmt in statements:
    stmt = stmt.strip()
    if stmt:
        try:
            cursor.execute(stmt)
        except Exception as e:
            print(f"Error executing: {stmt[:50]}... {e}")

conn.commit()
cursor.close()
conn.close()

print("Database and tables created successfully.")