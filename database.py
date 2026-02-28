"""
database.py

This module handles the database connection using MySQL connector.
It ensures a single reusable connection throughout the application.
"""

import mysql.connector
from config import DB_CONFIG


class Database:
    """
    Database class manages MySQL connection.
    """

    def __init__(self):
        # Initialize connection variable
        self.connection = None

    def connect(self):
        """
        Establish connection to MySQL database.
        """
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            print("Database connected successfully!")
        except Exception as e:
            print("Error connecting to database:", e)

    def get_connection(self):
        """
        Returns active connection.
        Creates one if not already created.
        """
        if not self.connection:
            self.connect()
        return self.connection