import mysql.connector
from mysql.connector.connection_cext import CMySQLConnection


class DatabaseFactory:
    def __init__(self):
        self.object = None

    def get_mysql_database(self) -> CMySQLConnection:
        """This method generates a database connection and returns to the caller."""
        if self.object is None:
            db = mysql.connector.connect(
                host="127.0.0.1", user="root", password="sagar", database="game"
            )
            return db
        return self.object
