'''
Game Execution will start from here!
'''
from status import Status
from arts import welcome
from colorama import init

if __name__ == '__main__':
    init()
    welcome()
    Game = Status()
    Game.start_game()