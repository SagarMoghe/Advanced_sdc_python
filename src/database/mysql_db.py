from abc import ABC

from mysql_factory import Mysql_Factory
from src.leagueObjectModel.player import Player
from src.leagueObjectModel.league import League
from typing import Type
from src.database.database import DatabaseOperations


class mysql_db(DatabaseOperations):
    def __init__(self):
        # self.connection = Mysql_Factory('config.env')
        pass

    def save_player(self, player: type[Player]) -> bool:
        print(f'player {player.name} saved with id {player.id}')
        return True

    def save_league(self, league: type(League)) -> bool:
        print(f'league {league.name} saved with id {league.id}')
        return True


p = Player("Sagar")
mysql_db().save_player(p)
