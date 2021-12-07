import pyfiglet
from colorama import Fore


class TitleScreen():

    def __init__(self, title):
        self.title = title
        self.titleFont = "big"
        self.width = 122
        self.color = None
        self.bannerText = []
        self.bannerColor = None
        self.caption = None
    
    def add_banner_line(self, bannerText):
        self.bannerText.append(bannerText)

    def draw_title_screen(self):
        if self.title is not None:
            t = pyfiglet.figlet_format(self.title, font=self.titleFont, width=self.width, justify="center")
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
            print(t + Fore.RESET + "\033[F")

            # Print Caption if there is one
            if self.caption is not None:
                print("\033[F" + self.caption)

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
                    self.bannerText[i] = "*" + (" " * int(((self.width - len(self.bannerText[i]))/2)-1)) + self.bannerText[i] + (" " * int(((self.width - len(self.bannerText[i]))/2)-2)) + "*"
                    print(self.bannerText[i])

                for x in range(1, self.width):
                    print('*', end='', flush=True)

            # Reset Banner Color Selection
            print(Fore.RESET)

def main():

    testScreen = TitleScreen(title="E L E A N O R ' S\nA D V E N T U R E")
    testScreen.color = "yellow"
    testScreen.caption = "Version 0.1a"
    testScreen.width = 100
    #testScreen.titleFont = "doom"
    testScreen.add_banner_line("TEST")
    testScreen.add_banner_line("Test 2")
    testScreen.bannerColor = "red"
    testScreen.draw_title_screen()


if __name__ == '__main__':
    main()