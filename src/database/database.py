from abc import ABC, abstractmethod


class DatabaseOperations(ABC):
    """This class deals with all the abstract methods of the database
    operations"""

    @abstractmethod
    def save_player(self, player) -> bool:
        """This method will save the player object to the database"""
        raise NotImplementedError

    @abstractmethod
    def save_manager(self, manager) -> bool:
        """This method will save the player object to the database"""
        raise NotImplementedError

    @abstractmethod
    def save_coach(self, coach) -> bool:
        """This method will save the player object to the database"""
        raise NotImplementedError

    @abstractmethod
    def save_team(self, team) -> bool:
        """This method will save the team object to the database"""
        raise NotImplementedError

    @abstractmethod
    def save_division(self, division) -> bool:
        """This method will save the division object to the database"""

    @abstractmethod
    def save_conference(self, conference) -> bool:
        """This method will save the conference object to the database"""
        raise NotImplementedError

    @abstractmethod
    def save_league(self, league) -> bool:
        """This method will save the league object to the database"""
        raise NotImplementedError

    @abstractmethod
    def update_player(self, player) -> bool:
        """This method will modify the player object to the database"""
        raise NotImplementedError

    @abstractmethod
    def update_manager(self, manager) -> bool:
        """This method will modify the manager object to the database"""

    @abstractmethod
    def update_coach(self, coach) -> bool:
        """This method will modify the coach object to the database"""
        raise NotImplementedError

    @abstractmethod
    def update_team(self, team) -> bool:
        """This method will modify the team object to the database"""
        raise NotImplementedError

    @abstractmethod
    def update_division(self, division) -> bool:
        """This method will modify the division object to the database"""
        raise NotImplementedError

    @abstractmethod
    def update_conference(self, conference) -> bool:
        """This method will modify the conference object to the database"""
        raise NotImplementedError

    @abstractmethod
    def update_league(self, league) -> bool:
        """This method will modify the league object to the database"""
        raise NotImplementedError

    @abstractmethod
    def load_player(self, team_id) -> bool:
        """This method will modify the player object to the database"""
        raise NotImplementedError

    @abstractmethod
    def load_team(self, division_id) -> bool:
        """This method will modify the team object to the database"""
        raise NotImplementedError

    @abstractmethod
    def load_division(self, conference_id) -> bool:
        """This method will modify the division object to the database"""
        raise NotImplementedError

    @abstractmethod
    def load_conference(self, league_id) -> bool:
        """This method will modify the conference object to the database"""
        raise NotImplementedError

    @abstractmethod
    def load_league(self) -> bool:
        """This method will modify the league object to the database"""
        raise NotImplementedError

    @abstractmethod
    def load_manager(self, manager) -> bool:
        """This method will load the manager object to the database"""
        raise NotImplementedError

    @abstractmethod
    def load_coach(self, coach) -> bool:
        """This method will load the coach object to the database"""
        raise NotImplementedError
