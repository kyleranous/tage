import pyfiglet
from colorama import Fore


class TitleScreen():

    def __init__(self, title):
        self.title = [title]
        self.titleFont = "big"
        self.width = 99
        self.color = None
        self.bannerText = []
        self.bannerColor = None
        self.caption = None
        self.menu = []
        self.menu_col = 3
   

    def add_title_line(self, title):
        self.title.append(title)


    def add_banner_line(self, bannerText):
        self.bannerText.append(bannerText)


    def add_menu_item(self, menuItem):
        
        if type(menuItem) is list:
            self.menu = self.menu + menuItem
        
        elif type(menuItem) is str:
            self.menu.append(menuItem)

        else:
            raise ValueError("Menu Items must be a String or List of Strings")


    def render_title(self):
        ''' Draws the Stylized Title '''

        if len(self.title) > 0:
            for t in self.title:
                t = pyfiglet.figlet_format(t, font=self.titleFont, width=self.width, justify="center")
                # Set title Color if there is one
                if self.color is not None:
                    if self.color.lower() == "blue":
                        print(Fore.BLUE)
                    elif self.color.lower() == "green":
                        print(Fore.GREEN)
                    elif self.color.lower() == "red":
                        print(Fore.RED)
                    elif self.color.lower() == "yellow":
                        print(Fore.YELLOW)
                    elif self.color.lower() == "black":
                        print(Fore.BLACK)
                    elif self.color.lower() == "cyan":
                        print(Fore.CYAN)
                    elif self.color.lower() == "magenta":
                        print(Fore.MAGENTA)
                    else:
                        raise ValueError(f"{self.color} is not a valid color selection")
            
                # Reset Title Color Selection
                print(t + Fore.RESET + "\033[F\033[F\033[F")


    def render_banner(self):

        # Set Banner Color if there is one
            if self.bannerColor is not None:
                if self.bannerColor.lower() == "blue":
                    print(Fore.BLUE, end='', flush=True)
                elif self.bannerColor.lower() == "green":
                    print(Fore.GREEN, end='', flush=True)
                elif self.bannerColor.lower() == "red":
                    print(Fore.RED, end='', flush=True)
                elif self.bannerColor.lower() == "yellow":
                    print(Fore.YELLOW, end='', flush=True)
                elif self.bannerColor.lower() == "black":
                    print(Fore.BLACK, end='', flush=True)
                elif self.bannerColor.lower() == "cyan":
                    print(Fore.CYAN, end='', flush=True)
                elif self.bannerColor.lower() == "magenta":
                    print(Fore.MAGENTA, end='', flush=True)
                else:
                    raise ValueError(f"{self.bannerColor} is not a valid color selection")

            if len(self.bannerText) > 0:
                for x in range(1, self.width):
                    print('*', end='', flush=True)

                print('\r')

                for i in range(0,len(self.bannerText)):
                    trailSpace = int(((self.width - len(self.bannerText[i]))/2-2))
                    
                    if len(self.bannerText[i]) % 2 != 0 and self.width % 2 == 0:
                        trailSpace += 1
                    elif len(self.bannerText[i]) % 2 == 0 and self.width % 2 != 0:
                        trailSpace += 1

                    self.bannerText[i] = "*" + (" " * int(((self.width - len(self.bannerText[i]))/2)-1)) + self.bannerText[i] + (" " * trailSpace) + "*"
                    print(self.bannerText[i])

                for x in range(1, self.width):
                    print('*', end='', flush=True)

            # Reset Banner Color Selection
            print(Fore.RESET)


    def render_menu(self):
        
        if len(self.menu) > 0:
            menuNum = 1
            tempMenu = self.menu
            tempStr = ""
            spacing = int(self.width / self.menu_col)
    
            while len(tempMenu) > 0:

                i = 0
                renderStr = ""
                while i < self.menu_col:

                    if len(tempMenu) > 0:
                        tempStr = tempMenu.pop(0)
                        spacingModifier = len(tempStr) + len(str(menuNum)) + 3
                        renderStr = renderStr + str(menuNum) + " - " + tempStr + (" " * (spacing - spacingModifier))
                        menuNum += 1
                    else:
                        break
                    i += 1
            
                print(renderStr)
            

    def render_title_screen(self):
            
            self.render_title()
            
            # Print Caption if there is one
            if self.caption is not None:
                print("\n" + self.caption)

            self.render_banner()
            
            self.render_menu()


def demo():

    testScreen = TitleScreen(title="G A M E")
    #testScreen = TitleScreen(title="")
    testScreen.add_title_line("T I T L E")
    testScreen.color = "green"
    testScreen.caption = "Version 0.1alpha(DEMO)"
    testScreen.width = 100
    #testScreen.titleFont = "doom"
    testScreen.add_banner_line("This is a banner!")
    testScreen.add_banner_line("Where you can put your game tagline.")
    testScreen.bannerColor = "blue"
    testScreen.add_menu_item(["Continue", "New Game", "Settings", "Quit", "Menu Item", "Another Menu Item"])
    testScreen.render_title_screen()


if __name__ == '__main__':
    demo()