from src.leagueObjectModel.team import Team


class objectFactory:

    def make_team(self, league_id: int, team_name: str):
        return Team(league_id=league_id, name=team_name)
