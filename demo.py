import os
import time
import sys
from colorama import Fore, Style
from map_tiles import MapTile, StartTile


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
        time.sleep(3)
        quit()
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
        return 0
    elif ans in noList:

      print("TEST")
    else:
        exitGame(errorMsg = "I'm sorry, I do not understand {}.".format(ans))

        
def main():
    #Setup Variables
    posX = 0
    posY = 0
    map = []
    errorMsg = None
    # Map Setup
    map.append([StartTile(name="Entryway"),
                MapTile(name="Closet"),
                MapTile(name="Book Shelf")])
    
    map.append([MapTile(name="Tipi"),
                MapTile(name="Window"),
                MapTile(name="Bed")])
    
    drawTitleScreen()

    map[0][0].shortDescription = "You are standing in an Entryway"
    map[0][1].shortDescription = "You are standing infront of a Closet"
    map[0][2].shortDescription = "You are standing infront of a Book Shelf"
    map[1][0].shortDescription = "You are standing infront of a White Canvas Tipi"
    map[1][1].shortDescription = "You are standing infront of a Window"
    map[1][2].shortDescription = "You are standing infront of a Bed"
    
    while True:
        # Load information
        print("\t" + map[posX][posY].name + "\n" + map[posX][posY].shortDescription + '\n')
        if errorMsg is not None:
            print(Fore.RED + errorMsg + '\n')
            errorMsg = None
            print(Fore.RESET)

        print(Style.BRIGHT)
        ans = input('> ')
        print(Style.RESET_ALL)
        
        # Check Answer
        if ans == "go north":

            if posY + 1 < len(map[posX]):
               posY = posY + 1

            else:
                errorMsg = "You can not go that way"

        elif ans == "go south":

            if posY >= 1:
                posY = posY - 1

            else:
                errorMsg = "You can not go that way"

        elif ans == "go east":

            if posX + 1 < len(map):
                posX = posX + 1

            else:
                errorMsg = "You can not go that way"

        elif ans == "go west":

            if posX >= 1:
                posX = posX - 1

            else:
                errorMsg = "You can not got that way"

        else:
            # Check to see if there is a special command for the tile
            # if ans is not equal to a special tile command then return an error
            errorMsg = "I'm sorry, I do not understand {}".format(ans)


if __name__ == '__main__':
   main()
