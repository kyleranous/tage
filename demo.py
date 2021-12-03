import os
import time
import sys
from colorama import Fore, Style


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
        # Call the room function
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
    entryWay()


def entryWay(errorMsg=None):
    
    print("\tYou are in the entry way.\n")
    if errorMsg is not None:
        print(Fore.RED + errorMsg)
        print(Fore.RESET)

    print(Style.BRIGHT)
    act = input('> ')
    print(Style.RESET_ALL)
    
    # North -> closet
    # East -> tipi
    # South -> Wall
    # West -> exitGame

    if act == "go north":
        closet()
    elif act == "go east":
        tipi()
    elif act == "go south":
        #clearConsole()
        entryWay(errorMsg="There is a wall")
    elif act == "go west":
        exitGame()
    else:
        entryWay(errorMsg = "I'm sorry, I do not understand {}.".format(act))


def closet(errorMsg = None):
    
    print("\tYou are standing infront of the closet.\n")
    if errorMsg is not None:
        print(Fore.RED + errorMsg)
        print(Fore.RESET)
    
    print(Style.BRIGHT)
    act = input('> ')
    print(Style.RESET_ALL + '\n')

    # North -> bookShelf
    # East -> window
    # South -> entryWay
    # West -> Wall
    if act == "go north":
        bookShelf()
    elif act == "go east":
        window()
    elif act == "go south":
        #clearConsole()
        entryWay()
    elif act == "go west":
        closet(errorMsg = "You can not go into the closet")
    else:
        entryWay(errorMsg = "I'm sorry, I do not understand {}.".format(act))
    

def bookShelf(errorMsg = None):

    print("\tYou are standing infront of a book shelf")

    if errorMsg is not None:
        print(Fore.RED + errorMsg)
        print(Fore.RESET)
    
    print(Style.BRIGHT)
    act = input('> ')
    print(Style.RESET_ALL + '\n')

    if act == "go north":
        bookShelf(errorMsg="There is a wall")
    elif act == "go east":
        bed()
    elif act == "go south":
        closet()
    elif act == "go west":
        bookShelf(errorMsg = "There is a wall")
    else:
        bookShelf(errorMsg = "I'm sorry, I do not understand {}.".format(act))


def bed(errorMsg = None):

    print("\tYou are standing infront of a bed")

    if errorMsg is not None:
        print(Fore.RED + errorMsg)
        print(Fore.RESET)
    
    print(Style.BRIGHT)
    act = input('> ')
    print(Style.RESET_ALL + '\n')

    # North -> Wall
    # East -> Wall
    # South -> Window
    # West -> bookShelf

    if act == "go north":
        bed(errorMsg = "There is a wall")
    elif act == "go east":
        bed(errorMsg = "There is a wall")
    elif act == "go south":
        window()
    elif act == "go west":
        bookShelf()
    else:
        bed(errorMsg = "I'm sorry, I do not understand {}.".format(act))


def window(errorMsg = None):

    print("You are standing infront of a window")

    if errorMsg is not None:
        print(Fore.RED + errorMsg)
        print(Fore.RESET)

    print(Style.BRIGHT)
    act = input('> ')
    print(Style.RESET_ALL + '\n')

    # North -> bed
    # East -> Wall
    # South -> tipi
    # West -> closet

    if act == "go north":
        bed()
    elif act == "go east":
        window(errorMsg = "You can not go out the window")
    elif act == "go south":
        tipi()
    elif act == "go west":
        closet()
    else:
        window(errorMsg = "I'm sorry, I do not understand {}.".format(act))
    

def tipi(errorMsg = None):

    print("You are standing infront of a tipi")

    if errorMsg is not None:
        print(Fore.RED + errorMsg)
        print(Fore.RESET)

    print(Style.BRIGHT)
    act = input('> ')
    print(Style.RESET_ALL + '\n')

    # North -> window
    # East -> Wall
    # South -> Wall
    # West -> entryWay

    if act == "go north":
        window()
    elif act == "go east":
        tipi(errorMsg = "There is a wall")
    elif act == "go south":
        tipi(errorMsg = "There is a wall")
    elif act == "go west":
        entryWay()
    else:
        tipi(errorMsg = "I'm sorry, I do not understand {}.".format(act))


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
        entryWay()
    else:
        exitGame(errorMsg = "I'm sorry, I do not understand {}.".format(ans))


if __name__ == '__main__':
    drawTitleScreen()