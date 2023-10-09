import pymysql
from dotenv import load_dotenv, find_dotenv
import os
from src.miscellaneous.custom_exceptions import *


class Mysql_Factory():

    def __init__(self, env_file):

        if not load_dotenv(find_dotenv(env_file)):
            raise MissingEnv("Fail to load .env file")
        self.username = os.getenv('USERNAME')
        self.password = os.getenv('PASSWORD')
        self.host = os.getenv('HOST')
        if not (self.username and self.password and self.host):
            raise MissingVariables(" Missing one of the USERNAME, PASSWORD, HOST variables")

        self.conn = None

    def get_connection(self):
        if self.conn and self.conn.open:
            print('returned old object')
            return self.conn
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.username,
                password=self.password,
            )
        except pymysql.err.OperationalError:
            raise FailedConnection("failed to establish connection to DB")

        print("new object")
        # To close the connection
        return self.conn

    def close_connection(self):
        if self.conn and self.conn.open:
            self.conn.close()
