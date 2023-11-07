class Player:
    def __init__(self, name: str):
        self.id = id(self)
        self.name = name
        print(f'player {self.name} created with id {self.id}')

# Player("sagar")
