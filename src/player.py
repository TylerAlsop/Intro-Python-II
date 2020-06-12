# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, current_room = None, inventory):
        self.current_room = current_room
        self.inventory = inventory

    # def __str__(self):
    #     output = f"You am currently in the {self.current_room}."
    #     return output


    # def __repr__(self):
    #     # also returns a string which helps devs understand how your object is structured.
    #     return f"self.name = {self.name} ; self.current_room =  {self.current_room}"

# player1 = Player("Tyler", "Sorcerer", "Outside")

# print(player1)