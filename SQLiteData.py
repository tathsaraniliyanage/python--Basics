import sqlite3

# Connect to (or create) a database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        city TEXT
    )
''')

# Insert data into the table
cursor.execute('''
    INSERT INTO users (name, age, city)
    VALUES ('Alice', 30, 'New York')
''')

# Commit and close the connection
conn.commit()
conn.close()
