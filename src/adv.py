from room import Room
from player import Player
from item import Item

########## ITEMS ##########
torch = Item("Torch", "It lights the way.")
knife = Item("Knife", "It cuts.")
paper_airplane = Item("Paper Airplane", "It flies.")
fly_swatter = Item("Fly Swatter", "It'll kill bugs.")
nothing = Item("Nothing", "This is an item, but there really is nothing.")


# Declare all the rooms
########## ROOMS ##########

outside = Room("Outside", "North of you, the mouth of the cave beckons.", [torch])

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [knife])

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [paper_airplane])

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [fly_swatter])

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [nothing])

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
print(f"Welcome to the game! Your player will begin in the Outside. \nYou can move North, East, South, and West by entering in 'n', 'e', 's', or 'w' respectively. \nEnter 'p' to pickup an item and 'd' to drop it. \nEnter 'q' to Quit.")

player = Player()
player.current_room = outside

# Write a loop that:
while True:
    print("###############################################################################")
    # * Prints the current room name

    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room)

    print("Items in this room:")
    if len(player.current_room.items) == 0:
        print("NONE")
    else:
        for item in player.current_room.items:
            print(f'  {item}')

    # * Waits for user input and decides what to do.
    choice = input("Please enter a command: ").lower().split(" ")

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    # If the user enters "q", quit the game.
    if len(choice) == 1:
        choice = choice[0]
        if (choice == 'q'):
            print("You have quit the game. Thanks for playing.")
            break

        elif choice == 'p':
            player.pickup_item()
            print("Your Inventory:")
            player.print_inventory()
        
        elif choice == 'd':
            player.drop_item()
            print("Your Inventory:")
            player.print_inventory()

        elif choice in {'n', 'e', 's', 'w'}:
            print(getattr(player.current_room, f'{choice}_to'))
            if getattr(player.current_room, f'{choice}_to') is not None:
                player.current_room = getattr(player.current_room, f'{choice}_to')
            # if hasattr(player.current_room, f'{choice}_to'):
            else:
                print("\nThat direction is not an option at this time.\n")

    if len(choice) == 2:
        command = choice[0]
        chosen_item = choice[1]

        if command == 'pickup':
            for item in player.current_room.items:
                if item.name == chosen_item:
                    player.pickup_item()
                    print("Your Inventory:")
                    player.print_inventory()
        if command == 'drop':
            for item in player.current_room.items:
                if item[0] == chosen_item:
                    player.drop_item()
                    print("Your Inventory:")
                    player.print_inventory()
    





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