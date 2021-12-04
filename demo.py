import os
import time
import sys
from colorama import Fore, Style
from map_tiles import MapTile


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
yesList = ['YEA', 'YES', 'Y', 'Yea', 'Yes', 'yea', 'yes', 'y']
noList = ['NAH', 'NO', 'N', 'Nah', 'No', 'n', 'nah', 'no']


def drawTitleScreen(errorMSG=None): # Draw the Title Screen
    clearConsole()
    print(Fore.GREEN + Style.BRIGHT)
    print("     /########  /##        /########   /######   /##   /##   /######   /#######   /##  /######")
    print("    | ##_____/ | ##       | ##_____/  /##__  ## | ### | ##  /##__  ## | ##__  ## | #/ /##__  ##")
    print("    | ##       | ##       | ##       | ##  \ ## | ####| ## | ##  \ ## | ##  \ ## |_/ | ##  \__/")
    print("    | #####    | ##       | #####    | ######## | ## ## ## | ##  | ## | #######/     |  ######")
    print("    | ##__/    | ##       | ##__/    | ##__  ## | ##  #### | ##  | ## | ##__  ##      \____  ##")
    print("    | ##       | ##       | ##       | ##  | ## | ##\  ### | ##  | ## | ##  \ ##      /##  \ ##")
    print("    | ######## | ######## | ######## | ##  | ## | ## \  ## |  ######/ | ##  | ##     |  ######/")
    print("    |________/ |________/ |________/ |__/  |__/ |__/  \__/  \______/  |__/  |__/      \______/")
    print("\n")
    print("  /######   /#######   /##    /##  /########  /##   /##  /########  /##   /##  /#######   /########")
    print(" /##__  ## | ##__  ## | ##   | ## | ##_____/ | ### | ## |__  ##__/ | ##  | ## | ##__  ## | ##_____/")
    print("| ##  \ ## | ##  \ ## | ##   | ## | ##       | ####| ##    | ##    | ##  | ## | ##  \ ## | ##")
    print("| ######## | ##  | ## |  ## / ##/ | #####    | ## ## ##    | ##    | ##  | ## | #######/ | #####")
    print("| ##__  ## | ##  | ##  \  ## ##/  | ##__/    | ##  ####    | ##    | ##  | ## | ##__  ## | ##__/")
    print("| ##  | ## | ##  | ##   \  ###/   | ##       | ##\  ###    | ##    | ##  | ## | ##  \ ## | ##")
    print("| ##  | ## | #######/    \  #/    | ######## | ## \  ##    | ##    |  ######/ | ##  | ## | ########")
    print("|__/  |__/ |_______/      \_/     |________/ |__/  \__/    |__/     \______/  |__/  |__/ |________/")
    print(Fore.RESET + Style.NORMAL + "\nVersion: 0.1a")
    print(Fore.BLUE + Style.BRIGHT)
    print("***************************************************************************************************")
    print("*                                             SOMETHING                                           *")
    print("*                                           INSPERATIONAL                                         *")
    print("***************************************************************************************************")
    print(Fore.RESET + Style.RESET_ALL)
    if errorMSG is not None:
        print(Fore.RED + errorMSG + Fore.RESET)

    print("Ready to start your adventure?\n")
    print(Style.BRIGHT)
    ans = input('> ')
    print(Style.RESET_ALL)

    if ans in yesList:
        clearConsole()
        print("Every day we write a new page to our story.")
        time.sleep(3)
        mapIntro()
        
    elif ans in noList:
        clearConsole()
        print("Tommorow I'll be all the things I tried to be today.")
    else:
        drawTitleScreen("I'm sorry, I do not understand {}.".format(ans))


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

def mapIntro():
    
    clearConsole()
    print( """\tINTRODUCTION TEXT TO ROOM
    """)
    print('\n')


def exitGame(errorMsg = None):
    
    if errorMsg is not None:
        print(Fore.RED + errorMsg)
        print(Fore.RESET)

    print("\tThis is a door leading out of the room. Would you like to leave?\n")

    print(Style.BRIGHT)
    ans = input('> ')
    print(Style.RESET_ALL)

    if ans in yesList:
        clearConsole()
        print("Tomorrow I'll be all the things I tried to be today")
    elif ans in noList:

      print("TEST")
    else:
        exitGame(errorMsg = "I'm sorry, I do not understand {}.".format(ans))

        
def main():
    #Setup Variables
    posX = 0
    posY = 0
    map = []
    # Map Setup
    map.append([MapTile(name="Entryway", shortDescription = "You are in the Entryway"),
                MapTile(name="Closet", shortDescription="You are standing infront of a closet"),
                MapTile(name="Book Shelf", shortDescription="You are standing infront of a bookshelf")])
    
    map.append([MapTile(name="Tipi", shortDescription="You are standing infront of a canvas tipi"),
                MapTile(name="Window", shortDescription="You are standing infront of a mirror"),
                MapTile(name="Bed", shortDescription="You are standing infront of a bed")])
    
    drawTitleScreen()

    print(map[posX][posY].shortDescription)


if __name__ == '__main__':
   main()
