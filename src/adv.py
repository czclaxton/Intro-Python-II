from room import Room
from player import Player
# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

rooms['outside'].w_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].w_to = rooms['overlook']
rooms['foyer'].d_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].a_to = rooms['foyer']
rooms['narrow'].w_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(rooms['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

choices = ['w', 'a', 's', 'd']

while True:
    print(f'Your current location is: {player.location.name} .')
    # User will pick a direction
    cmd = input("-> ")

    if cmd in choices:
        if hasattr(player.location, f'{cmd}_to'):
            new_room = getattr(player.location, f'{cmd}_to')
            player.move(new_room)

        else:
            print('That directions appears to be a dead end, try another direction...')
    elif cmd == "q":
        print('Bye!')
        break
    else:
        print('Invalid Command')
