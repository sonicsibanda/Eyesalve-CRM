import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'sonic123',
    )

# Prepare a cursor object
cursorObject = database.cursor()

# Create a Database
cursorObject.execute("CREATE DATABASE sonicco")

print("All Done!")