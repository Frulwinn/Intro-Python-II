from room import Room
from player import Player

# Declare all the rooms

room = {
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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

"""
returns the new room that the player moves to if the move was succesful
or returns to the current room if the move was not successful
"""
def try_direction(direction, current_room):
    attribute = direction + '_to'

    #see if the inputted direction is one we can move to
    #checks if current room as the attribute that is appended
    if hasattr(current_room, attribute):
        #if it has the attribute it gives you the room you are moving to, fetch the new room
        return getattr(current_room, attribute)

    else:
        print("You can't go that way!")
        return current_room

# Write a loop that:
while True:
#
# * Prints the current room name
    print(player.current_room.name)

# * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)

# * Waits for user input and decides what to do.
    #handles multiple words
    s = input("\n> ").lower().split()
    
    #check to see if the user inputted a one or two word command
    if len(s) == 1:
        #the user passed us a direction
        #grab the first charcter of the first word
        s = s[0][0]
        print(s)

        # If the user enters "q", quit the game.
        if s == 'q':
            print("See you next time!")
            break

        player.current_room = try_direction(s, player.current_room)
        
    elif len(s) == 2:
        #the user passed us a two word command
        #grab first word
        first_word = s[0]
        second_word = s[1]

        # if first_word in ['get', 'drop']:
            #do something with the second word here

    # Print an error message if the movement isn't allowed.
    else:
        print("I don't understand that")
        continue


    # if s == 'n':
    #     player.current_room = player.current_room.n_to
    # elif s == 's':
    #     player.current_room = player.current_room.s_to
    # elif s == 'e':
    #     player.current_room = player.current_room.e_to
    # elif s == 'w':
    #     player.current_room = player.current_room.w_to
    # else:
    #     print("Not a valid direction!")
    

    """
    North, South, East, West
    N S E W

    """
#
# If the user enters a cardinal direction, attempt to move to the room there.