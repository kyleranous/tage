import time
from colorama import Fore, Style
from tagemap import MapTile, StartTile
from tageplayer import Player
from tageitem import Item, Gold
import tagetitlescreen
import tageutils

# ToDo: Move clearConsole to a general utilities module
# ToDo: Fix Function Name from clearConsole to clear_console


# ToDo: Move yesList and noList to text_parser module
# ToDo: fix yesList and noList variable names to YES_LIST and NO_LIST
yesList = ['YEA', 'YES', 'Y', 'Yea', 'Yes', 'yea', 'yes', 'y']
noList = ['NAH', 'NO', 'N', 'Nah', 'No', 'n', 'nah', 'no']
INSPECT_LIST = ['inspect', 'look']


def draw_title_screen(errorMSG=None):  # Draw the Title Screen
    
    tageutils.clear_console()
    
    # Create Title Screen
    t = tagetitlescreen.TitleScreen("E L E A N O R ' S\nA D V E N T U R E")
    t.color = "green"
    t.caption = "Version 0.1alpha"
    t.add_banner_line("PLACEHOLDER")
    t.add_banner_line("TEXT")
    t.bannerColor = "blue"
    t.render_title_screen()

    if errorMSG is not None:
        print(Fore.RED + errorMSG + Fore.RESET)

    print("Ready to start your adventure?\n")
    print(Style.BRIGHT)
    ans = input('> ')
    print(Style.RESET_ALL)

    if ans.lower() in yesList:
        tageutils.clear_console()
        print("Every day we write a new page to our story.")
        time.sleep(3)
        map_intro()

    elif ans.lower() in noList or ans.lower() == "quit":
        tageutils.clear_console()
        print("Goodbye!")
        time.sleep(3)
        quit()
    else:
        draw_title_screen(f"I'm sorry, I do not understand {ans}.")


# Room Layout
#      _________________________
#     |            |            |
#     | bookShelf  |     bed    |
#     |            |            |
#     |            |            |
#     |------------+------------|        N
#     |            |            |        |
#     |   closet   |   window   |    W---+---E
#     |            |            |        |
#     |            |            |        S
#     |------------+------------|
#     |            |            |
#     |  entryWay  |    tipi    |
#     |            |            |
#     |____________|____________|


def map_intro():  # map_intro should be a function of the GameMap class

    tageutils.clear_console()
    print( """\tINTRODUCTION TEXT TO MAP""")
    print('\n')


def exit_game(errorMsg = None):

    if errorMsg is not None:
        print(Fore.RED + errorMsg)
        print(Fore.RESET)

    print("\tThis is a door leading out of the room. Would you like to leave?\n")

    print(Style.BRIGHT)
    ans = input('> ')
    print(Style.RESET_ALL)

    if ans.lower() in yesList:
        tageutils.clear_console()
        # Reset any special console text formatting
        print(Fore.RESET + Style.RESET_ALL)
        # Print Exit Message
        print("Tomorrow I'll be all the things I tried to be today")
        # Wait for 3 Seconds then load the title screen
        time.sleep(3)
        draw_title_screen()
        
    elif ans.lower() in noList:

        return

    else:
        exit_game(errorMsg = f"I'm sorry, I do not understand {ans}.")


def main():
    #Setup Variables
    posX = 0
    posY = 0
    mapMat = []
    errorMsg = None
    specialMsg = None

    # Demo Charecter Setup
    demoPlayer = Player("Ellie")

    # Map Setup
    mapMat.append([StartTile(name="Entryway"),
                MapTile(name="Closet"),
                MapTile(name="Book Shelf")])

    mapMat.append([MapTile(name="Tipi"),
                MapTile(name="Window"),
                MapTile(name="Bed")])

    draw_title_screen()

    mapMat[0][0].shortDescription = "You are standing in an Entryway"
    mapMat[0][1].shortDescription = "You are standing in front of a Closet"
    mapMat[0][2].shortDescription = "You are standing in front of a Book Shelf"
    mapMat[1][0].shortDescription = "You are standing in front of a White Canvas Tipi"
    mapMat[1][1].shortDescription = "You are standing in front of a Window"
    mapMat[1][2].shortDescription = "You are standing in front of a Bed"


    # Create Special  tile commands
    mapMat[1][2].tile_inspect = {  # Inspection for bed tile
        "bed" : "The bed is full of stuffed animals.",
        "Stuffed Animals" : "There is a Unicorn and a purple lama"
    }

    mapMat[1][1].tile_inspect = {  # Inspection for window tile
        "window" : "There are horses playing in a stable and a distant mountain range."
    }

    mapMat[0][1].tile_inspect = {  # Inspection for Closet tile
        "closet" : "The closet is empty, but might be a good place to store things."
    }

    mapMat[0][2].tile_inspect = {  # Inspection for book shelf tile
        "shelf" : "The Book Shelf has lots of room for books, think of all the adventures that would be!"
    }

    mapMat[1][0].tile_inspect = { # Inspection for tipi tile
        "tipi" : "The tipi has blankets and pillows on the floor, looks like a comfy place to read."
    }
    
    i = Item("testItem", "Test Item", 0)
    g = Gold(100)
    
    print(type(g))
    # Create an Item and 

    #mapMat[0][2].map_items()


    while True: # Active Game Loop
        # Load information
        posX = demoPlayer.player_pos()[0]
        posY = demoPlayer.player_pos()[1]

        print("\t" + mapMat[posX][posY].name + "\n" + mapMat[posX][posY].shortDescription + '\n')
        
        if specialMsg is not None:  # If the tile has a Special Message, print it
            print(specialMsg + '\n')
            specialMsg = None

        if errorMsg is not None:
            print(Fore.RED + errorMsg + '\n')
            errorMsg = None
            print(Fore.RESET)

        print(Style.BRIGHT)
        ans = input('> ')
        print(Style.RESET_ALL)

        # Check Answer
        if ans.lower() == "go north":

            if posY + 1 < len(mapMat[posX]):
                demoPlayer.posY += 1

            else:
                errorMsg = "You can not go that way"

        elif ans.lower() == "go south":

            if posY >= 1:
                demoPlayer.posY -= 1

            else:
                errorMsg = "You can not go that way"

        elif ans.lower() == "go east":

            if posX + 1 < len(mapMat):
                demoPlayer.posX += 1

            else:
                errorMsg = "You can not go that way"

        elif ans.lower() == "go west":

            if posX >= 1:
                demoPlayer.posX -= 1

            elif posX == 0 and posY == 0:
                # Use this as an exit tile
                exit_game()

            else:
                errorMsg = "You can not got that way"

        elif ans.split()[0].lower() in INSPECT_LIST:
            # Check to see if there are special inspect items in the current map tile
            if mapMat[posX][posY].inspect_list():
                # Check to see if the item being called is in the map tiles inspect list
                if ans.split()[-1].lower() in mapMat[posX][posY].tile_inspect.keys():
                    # Return to the Tile with a special message
                    specialMsg = mapMat[posX][posY].tile_inspect[ans.split()[-1].lower()]
                else:
                    errorMsg = f"I'm sorry, I do not understand {ans}"
            else:# if ans is not equal to a special tile command then return an error
                errorMsg = f"I'm sorry, I do not understand {ans}"
        else:
            errorMsg = f"I'm sorry, I do not understand {ans}"


if __name__ == '__main__':
    main()
