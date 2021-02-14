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
    print_art(BRICKBREAKER2,Fore.GREEN)
    print_art(MYNAME,Fore.GREEN)
    print_art(INSTRUCTION,Fore.BLUE)
    print_art(GAMEINSTRUCTION,Fore.BLUE)
    ch = Get()
    while True:
        ch1 =input_to(ch,1000)
        if ch1=='g' or ch1=='G':
            break
        elif ch1=='q' or ch1=='Q':
            quit()