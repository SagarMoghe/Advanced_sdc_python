from src.objectFactory import database_object_factory
from abc import ABC, abstractmethod


class DatabaseOperations(ABC):
    """This class deals with all the abstract methods of the database
    operations"""

    @abstractmethod
    def load_player(self, player) -> bool:
        """This method will save the player object to the database"""

    @abstractmethod
    def load_team(self, team) -> bool:
        """This method will save the team object to the database"""

    @abstractmethod
    def load_division(self, division) -> bool:
        """This method will save the division object to the database"""

    @abstractmethod
    def load_conference(self, conference) -> bool:
        """This method will save the conference object to the database"""

    @abstractmethod
    def load_league(self, league) -> bool:
        """This method will save the league object to the database"""

    @abstractmethod
    def update_player(self, player) -> bool:
        """This method will modify the player object to the database"""

    @abstractmethod
    def update_team(self, team) -> bool:
        """This method will modify the team object to the database"""

    @abstractmethod
    def update_division(self, division) -> bool:
        """This method will modify the division object to the database"""

    @abstractmethod
    def update_conference(self, conference) -> bool:
        """This method will modify the conference object to the database"""

    @abstractmethod
    def update_league(self, league) -> bool:
        """This method will modify the league object to the database"""

    @abstractmethod
    def load_player(self, player_id) -> bool:
        """This method will modify the player object to the database"""

    @abstractmethod
    def load_team(self, team) -> bool:
        """This method will modify the team object to the database"""

    @abstractmethod
    def load_division(self, division) -> bool:
        """This method will modify the division object to the database"""

    @abstractmethod
    def load_conference(self, conference) -> bool:
        """This method will modify the conference object to the database"""

    @abstractmethod
    def load_league(self, league) -> bool:
        """This method will modify the league object to the database"""
