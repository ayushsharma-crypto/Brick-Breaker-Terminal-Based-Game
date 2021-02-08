'''
Game Execution will start from here!
'''
from status import Status
from colorama import init,Fore,Back,Style

if __name__ == '__main__':
    init()
    Game = Status()
    Game.start_game()