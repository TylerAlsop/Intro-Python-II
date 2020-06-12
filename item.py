class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}."

    def repr(self):
        return f'self.name = {self.name} ; self.description = {self.description}'

