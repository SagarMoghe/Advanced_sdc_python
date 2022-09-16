import mysql.connector
from mysql.connector.connection_cext import CMySQLConnection


class DatabaseFactory:
    def __init__(self):
        self.object = None

    def get_mysql_database(self) -> CMySQLConnection:
        """This method generates a database connection and returns to the
        caller."""
        if self.object is None:
            try:
                self.object = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="admin",
                    database="game_db",
                )
            except Exception:
                print("Failed to generate connection to db")
            return self.object
        return self.object
