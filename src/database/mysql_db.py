from mysql_factory import Mysql_Factory
from src.leagueObjectModel.player import Player
from typing import Type
from src.database.database import DatabaseOperations


class mysql_db(DatabaseOperations):
    def __init__(self):
        self.connection = Mysql_Factory('config.env').get_connection()

    def save_player(self, p: type[Player]):
        insert_query = """
        INSERT INTO simulation.player_table (player_id, player_name)
        values (%s, %s)
        ON DUPLICATE KEY UPDATE player_id = %s, player_name = %s;"""
        with self.connection.cursor() as cursor:
            values = (p.id, p.name, p.id, p.name)
            cursor.execute(insert_query, values)
            self.connection.commit()
        print(f'player {p.name} saved with id {p.id}')


p = Player("Sagar")
p2 = Player("Moghe")
mysql_db().save_player(p)
mysql_db().save_player(p2)
p.set_name("updated_sagar")
mysql_db().save_player(p)
