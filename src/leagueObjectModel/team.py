from src.database.database import DatabaseOperations

class Team:
    def __init__(self, league_id: int, name: str):
        self.league_id = league_id
        self.name = name
        self.id = id(self)
        print(f'new team {self.name} created with id {self.id}')
        self.players = {}

    def save(self):
        for player in self.players.values():
            player.save()

        DatabaseOperations.save_team(self)


