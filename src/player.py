# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, title, location):
        self.name = name
        self.title = title
        self.location = location

    def __str__(self):
        output = f"Hello! My name is, {self.name}. I am a {self.title}. I am currently in the {self.location}."
        return output


    def __repr__(self):
        # also returns a string which helps devs understand how your object is structured.
        return f"self.name = {self.name} ; self.title = {self.title}"

player1 = Player("Tyler", "Sorcerer", "Outside")

print(player1)