'''
Game Execution will start from here!
'''
from os import system
from status import Status
from colorama import init,Fore,Back,Style

init()
Game = Status()
while(1):
    system('clear')
    Game.print_status()
