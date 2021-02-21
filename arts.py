from colorama import Fore,Style
import os
import sys
from input import input_to,Get

BRICKBREAKER2 = [

"  ____  _____  _____ _____ _  __     ____  _____  ______          _  ________ _____  ",
" |  _ \|  __ \|_   _/ ____| |/ /    |  _ \|  __ \|  ____|   /\   | |/ /  ____|  __ \ ",
" | |_) | |__) | | || |    | ' /_____| |_) | |__) | |__     /  \  | ' /| |__  | |__) |",
" |  _ <|  _  /  | || |    |  < _____|  _ <|  _  /|  __|   / /\ \ |  < |  __| |  _  / ",
" | |_) | | \ \ _| || |____| . \     | |_) | | \ \| |____ / ____ \| . \| |____| | \ \ ",
" |____/|_|  \_\_____\_____|_|\_\    |____/|_|  \_\______/_/    \_\_|\_\______|_|  \_\\",
"                                                                                     ",
"                                                                                     ",
"                                                                                     ",
"                                                                                     ",

]



MYNAME = [

"  _                  __       __         __          ",
" |_\\\\_/    /\\\\_//  \(_ |__|  (_ |__| /\ |__)|\/| /\  ",
" |_/ |    /--\| \__/__)|  |  __)|  |/--\|  \|  |/--\ ",
"                                            ",

]



INSTRUCTION = [

"   _   _   _   _   _   _   _   _   _   _   _  ",
"  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ ",
" ( I | N | S | T | R | U | C | T | I | O | N )",
"  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ ",

]

GAMEINSTRUCTION =[
    "                                           ",
    "  ___________________________________________",
    " |                                           |",
    " | Press g or G to start game                |",
    " |                                           |",
    " | Press q or Q to quit game                 |",
    " |                                           |",
    " | Press Spacebar to release the ball        |",
    " |                                           |",
    " | Press a or A to move paddle left          |",
    " |                                           |",
    " | Press d or D to move paddle right         |",
    " |                                           |",
    " | Total 3 lives                             |",
    " |                                           |",
    " | Total 3 stages or level                   |",
    " |                                           |",
    " | somemore...                               |",
    " |                                           |",
    " | Score +                                   |",
    " |                                           |",
    " | Bricks type                               |",
    " |___________________________________________|"
]


GAMECOMPLETED = [
"   ___   _   __  __ ___    ___ ___  __  __ ___ _    ___ _____ ___ ___  ",
"  / __| /_\ |  \/  | __|  / __/ _ \|  \/  | _ \ |  | __|_   _| __|   \ ",
" | (_ |/ _ \| |\/| | _|  | (_| (_) | |\/| |  _/ |__| _|  | | | _|| |) |",
"  \___/_/ \_\_|  |_|___|  \___\___/|_|  |_|_| |____|___| |_| |___|___/ ",
"                                                                       ",
"                                                                       ",
"                                                                       ",
]

PLAYAGAIN = [
    
"                           ___     ___                                                    ",
"  _____     _             |_  |   |_  |   _              _                        _       ",
" |   __|___| |_ ___ ___     |_|___  |_|  | |_ ___    ___| |___ _ _    ___ ___ ___|_|___   ",
" |   __|   |  _| -_|  _|      |  _|      |  _| . |  | . | | .'| | |  | .'| . | .'| |   |_ ",
" |_____|_|_|_| |___|_|        |_|        |_| |___|  |  _|_|__,|_  |  |__,|_  |__,|_|_|_|_|",
"                                                    |_|       |___|      |___|            "
"                                                                           "
"                                                                           "

]

OTHERWISE = [

"                                         ",
"  _____ _                    _           ",
" |   __| |___ ___    ___ ___| |_ ___ ___ ",
" |   __| |_ -| -_|  | -_|   |  _| -_|  _|",
" |_____|_|___|___|  |___|_|_|_| |___|_|  ",
"                                         "
"                                         "
"                                         "

]


SCORE = [
" +-+-+-+-+-+ +-+",          
" |S|C|O|R|E| |:|",          
" +-+-+-+-+-+ +-+",
]

LIVES =[        
" +-+-+-+-+-+ +-+",          
" |L|I|V|E|S| |:|",            
" +-+-+-+-+-+-+-+",    

]

TIME = [
" +-+-+-+-+-+-+",
" |T|I|M|E| |:|",
" +-+-+-+-+-+-+",
]

MAXSTAGE = [
" +-+-+-+-+-+-+-+-+-+-+-+",
" |M|A|X|-|S|T|A|G|E| |:|",        
" +-+-+-+-+-+-+-+-+-+ +-+",
]



def print_art(art: list,color):
    '''
    Just print out the list
    '''
    for line in art:
        print(color,Style.BRIGHT,end="")
        for i in line:
            print(i,end="")
        print(Style.RESET_ALL)



def welcome():
    '''
    Clear the screen and show instruction
    '''
    sys.stdout.flush()
    sys.stdin.flush()
    os.system('tput reset')
    print_art(BRICKBREAKER2,Fore.YELLOW)
    print_art(MYNAME,Fore.YELLOW)
    print_art(INSTRUCTION,Fore.GREEN)
    print_art(GAMEINSTRUCTION,Fore.GREEN)
    ch = Get()
    while True:
        ch1 =input_to(ch,1000)
        if ch1=='g' or ch1=='G':
            break
        elif ch1=='q' or ch1=='Q':
            quit()



def show_result(stat_dict):
    '''
    This function will show the post-game things
    '''
    sys.stdout.flush()
    sys.stdin.flush()
    os.system('tput reset')
    st = stat_dict['STAGE']
    if stat_dict['STAGE']==4:
        st = 3
    print_art(GAMECOMPLETED,Fore.GREEN)
    print(Fore.BLUE,Style.BRIGHT)
    print("\tXXXXXXXXXXXXXXXXXXXXXXXX")
    print("\n\t|->  SCORE    :  ", stat_dict['SCORE'])
    print("\n\t|->  LIVES    :  ", stat_dict['LIVES'])
    print("\n\t|->  TIME     :  ", stat_dict['TIME'])
    print("\n\t|->  MAXSTAGE :  ", st)
    print("\n")
    print("\tXXXXXXXXXXXXXXXXXXXXXXXX")
    print("\n\n\n")
    print(Style.RESET_ALL)

    print_art(PLAYAGAIN,Fore.RED)
    print_art(OTHERWISE,Fore.RED)
    ch = input()
    if ch != 'r' and ch!='R':
        quit()