# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        output = f"Welcome to the {self.name}. {self.description}"
        return output


    def __repr__(self):
        # also returns a string which helps devs understand how your object is structured.
        return f"self.name = {self.name} ; self.description = {self.description}"

# room1 = Room("Living Room", "This is where we relax and play games.")

# print(room1)