import mysql.connector
from config import DB_CONFIG


class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            print("Database connected successfully!")
        except Exception as e:
            print("Error connecting to database:", e)

    def get_connection(self):
        if not self.connection:
            self.connect()
        return self.connection