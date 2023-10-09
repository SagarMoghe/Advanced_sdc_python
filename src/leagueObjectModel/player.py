class Player:
    def __init__(self, name: str):
        self.id = id(self)
        self.name = name
        print(f'player {self.name} created with id {self.id}')

    def set_name(self, name: str):
        self.name = name
        print(f"player with id {self.id} name updated to {self.name}")
# Player("sagar")
