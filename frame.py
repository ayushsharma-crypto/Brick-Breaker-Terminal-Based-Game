import os
from status import Status
import sys
from colorama import Fore,Back,Style
from constants import FRAMEHEIGHT,FRAMEWIDTH

class Frame:
    def __init__(self, status: Status):
        self.status = status
        self.current_frame = self.initial_current_frame(FRAMEWIDTH,FRAMEHEIGHT)        


    def display_title(self):
        '''
        This will display the status of the game as the title on terminal.
        '''
        os.system('tput reset')
        inst_status = self.status.ret_status()
        print(
            Fore.BLUE + Style.BRIGHT +
            (
                "\n  LIVES: " +
                str(inst_status['LIVES']) + 
                "\t\t\t\tSTAGE: " + 
                str(inst_status['STAGE']) +
                "\t\t\t\tSCORE: " + 
                str(inst_status['SCORE']) + 
                "\t\t\t\tTIME: " + 
                str(inst_status['TIME'])
            )+ Style.RESET_ALL
        )

        
    def display(self):
        '''
        Renders the current Frame of the Game
        '''
        sys.stdout.flush()
        self.display_title()
        for h in range(len(self.current_frame)):
            print("".join(self.current_frame[h]))
        


    def initial_current_frame(self,width,height):
        '''
        Initialises the Frame of the Game
        '''
        container = [ [ " " for i in range(width) ] for j in range(height) ]
        
        for w in range(1,width-1):
            container[0][w]=f"{Fore.MAGENTA}{Style.BRIGHT}_{Style.RESET_ALL}"
            container[height-1][w]=f"{Fore.MAGENTA}{Style.BRIGHT}^{Style.RESET_ALL}"
        
        for h in range(1,height-1):
            container[h][0]=f"{Fore.MAGENTA}{Style.BRIGHT}|{Style.RESET_ALL}"
            container[h][width-1]=f"{Fore.MAGENTA}{Style.BRIGHT}|{Style.RESET_ALL}"

        return container


    
    def update_frame(self,point,shape,dimension):
        '''
        It update the current Frame of the Game.
        Basically for add another object on top of it base frame.
        '''
        for h in range(dimension.height):
            for w in range(dimension.width):
                self.current_frame[point.y + h][point.x + w] = shape[h][w]
    


    def restore_frame(self,point,shape,dimension,old_point,old_shape,old_dimension):
        '''
        It restore the Frame of the Game.
        Basically for moving another object on top of it base frame.
        '''
        for h in range(old_dimension.height):
            for w in range(old_dimension.width):
                self.current_frame[old_point.y + h][old_point.x + w] = " "
                # print(
                #     f"\033[{old_point.x + w};{old_point.y + h+1}H"+"h",end =""
                #     )
        for h in range(dimension.height):
            for w in range(dimension.width):
                self.current_frame[point.y + h][point.x + w] = shape[h][w]

    