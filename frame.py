import os
from colorama import Fore,Back,Style
from constants import FRAMEHEIGHT,FRAMEWIDTH

class Frame:
    def __init__(self, status):
        self.status = status

    def display_title(self):
        '''
        This will display the status of the game as the title on terminal.
        '''
        os.system('clear')
        inst_status = self.status.ret_status()
        print(
            Fore.BLUE + Style.BRIGHT +
            (
                "  SCORE: " +
                str(inst_status['SCORE']) + 
                "\t\t\t\t\tLIVES: " + 
                str(inst_status['LIVES']) + 
                "\t\t\t\t\tTIME: " + 
                str(inst_status['TIME']) + 
                "\t\t\t\t\tSTAGE: " + 
                str(inst_status['STAGE'])
            )+ 
            Style.RESET_ALL
        )
    
    def display_container(self,width,height):
        
        '''
        '''
        container = [ [ "" for i in range(width) ] for j in range(height) ]
        for h in range(height):
            for w in range(width):
                container[h][w] = " "
                
        for w in range(1,width-1):
            container[0][w]=f"{Fore.MAGENTA}{Style.BRIGHT}_{Style.RESET_ALL}"

        for w in range(1,width-1):
            container[height-1][w]=f"{Fore.MAGENTA}{Style.BRIGHT}^{Style.RESET_ALL}"

        for h in range(1,height-1):
            container[h][0]=f"{Fore.MAGENTA}{Style.BRIGHT}|{Style.RESET_ALL}"
            container[h][width-1]=f"{Fore.MAGENTA}{Style.BRIGHT}|{Style.RESET_ALL}"

        for h in range(height):
            print("".join(container[h]))
        
    def display(self):
        '''
        '''
        self.display_title()
        self.display_container(FRAMEWIDTH,FRAMEHEIGHT)
        