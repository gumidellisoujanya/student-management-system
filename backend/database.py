import sqlite3

conn = sqlite3.connect('students.db')
c = conn.cursor()
# Create tables here
conn.close()