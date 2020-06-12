from room import Room
from player import Player

# Declare all the rooms


outside = Room("Outside", "North of you, the mouth of the cave beckons.")

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

# plains = Room("Plains", """You're headed out to the middle of no-where!""")


# Link rooms together

outside.n_to = foyer
# outside.s_to = plains
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print(f"Welcome to the game! Your player will begin in the Outside. You can move North, East, South, and West by entering in 'n', 'e', 's', or 'w' respectively. Enter 'q' to Quit.")

player = Player()
player.current_room = outside

# Write a loop that:
while True:

    # * Prints the current room name
    print(player.current_room)

    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)

    # * Waits for user input and decides what to do.
    choice = input("Please choose a direction to move: ")

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if (choice == 'q'):
        print("You have quit the game. Thanks for playing.")
        break

    elif choice in {'n', 'e', 's', 'w'}:
        if hasattr(player.current_room, f'{choice}_to'):
            player.current_room = getattr(player.current_room, f'{choice}_to')
        # else:
        #     print("That direction is not an option at this time.")
        #     continue

    # If the user enters "q", quit the game.




#*** ALTERNATIVE WAY ***#


# if choice == 'n':
#     if player.current_room.n_to is not None:
#         player.current_room = player.current_room.n_to

# elif choice == 'e':
#     if player.current_room.e_to is not None:
#         player.current_room = player.current_room.e_to

# elif choice == 's':
#     if player.current_room.s_to is not None:
#         player.current_room = player.current_room.s_to

# elif choice == 'w':
#     if player.current_room.w_to is not None:
#         player.current_room = player.current_room.w_to