from src.objectFactory.league_factory import objectFactory
from src.leagueObjectModel.team import Team
from src.database.database import DatabaseOperations



class League:
    def __init__(self, name: str):
        self.id = id(self)
        self.name = name
        print(f'League {self.name} created with id {self.id}')
        self.teams = {}

    def create_team(self, team_name: str):
        team = objectFactory.make_team(league_id=self.id, team_name=team_name)
        self.teams[team.id] = team

    def add_team(self, team: type(Team)):
        team.league_id = id(self)
        self.teams[team.id] = team

    def get_all_teams(self):
        return ((t.id, t.name) for t in self.teams.values())

    def get_team(self, team_id: int):
        team = self.teams.get(team_id, None)

        if team:
            return team
        else:
            raise KeyError(f"league does not contain the team with id {team_id}")

    def save(self):
        for team in self.teams.values():
            team.save()
        DatabaseOperations().save_league(league=self)

