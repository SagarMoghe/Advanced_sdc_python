from mysql_factory import Mysql_Factory
from src.leagueObjectModel.player import Player
from typing import Type
from src.database.database import DatabaseOperations


class mysql_db(DatabaseOperations):
    def __init__(self):
        # self.connection = Mysql_Factory('config.env')
        pass

    def save_player(self, p: type[Player]):
        print(f'player {p.name} saved with id {p.id}')


p = Player("Sagar")
mysql_db().save_player(p)