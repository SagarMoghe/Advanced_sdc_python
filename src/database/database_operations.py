from src.objectFactory import database_object_factory
from abc import ABC, abstractmethod


class DatabaseOperations(ABC):
    """This class deals with all the abstract methods of the database
    operations"""

    @abstractmethod
    def save_player(self, player) -> bool:
        """This method will save the player object to the database"""
        raise NotImplementedError

    @abstractmethod
    def delete_player(self, player) -> bool:
        """This method will save the player object to the database"""
        raise NotImplementedError
