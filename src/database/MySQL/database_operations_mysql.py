from src.database.database_operations import DatabaseOperations


class mySQL(DatabaseOperations):
    def __init__(self, connection):
        if connection is None:
            print("Connection is None")
            raise ValueError
        self.connection = connection

    def save_player(self, player):
        try:
            cursor = self.connection.cursor()
            cursor.callproc('save_player', player.id, player.name, player.team)
            return True
        except Exception:
            return False
        finally:
            self.connection.close()

    def delete_player(self, player):
        try:
            cursor = self.connection.cursor()
            cursor.callproc('delete_player', player.id)
            return True
        except Exception:
            return False
        finally:
            self.connection.close()
