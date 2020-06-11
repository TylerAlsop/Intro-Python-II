# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None


    def __str__(self):
        output = f'You have entered the {self.name}: {self.description}\n'
        if self.n_to:
            output += f'The name of the room to the North is the: {self.n_to.name} \n'
        if self.e_to:
            output += f'The name of the room to the East is the: {self.e_to.name} \n'
        if self.s_to:
            output += f'The name of the room to the South is the: {self.s_to.name} \n'
        if self.w_to:
            output += f'The name of the room to the West is the: {self.w_to.name} \n'

        return output


    # def __repr__(self):
    #     # also returns a string which helps devs understand how your object is structured.
    #     return f"self.name = {self.name} ; self.description = {self.description}"

# room1 = Room("Living Room", "This is where we relax and play games.")

# print(room1)