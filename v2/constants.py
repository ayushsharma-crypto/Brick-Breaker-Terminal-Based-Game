MAXLIFE = 3
FRAMEWIDTH = 150
FRAMEHEIGHT = 45
PADDLEWIDTH = 20
PADDLEHEIGHT = 1
EXPANDPADDLE = 25
SHRINKPADDLE = 15
PADDLESTEPX = 2
BALLSTEPX = 1
BALLSTEPY = 1
BALLSTEPTP = 0.1
BRICKWIDTH = 15
BRICKHEIGHT = 2
LAYOUTWIDTH = 130
LAYOUTHEIGHT = 15
LAYOUTXOFFSET = 12
LAYOUTYOFFSET = 3
BASICSCOREINCREMENT=5
MAXSTAGE = 5
SHIFTDOWN = 1
SHIFTDOWNSTARTAFTER = 60
POWERUPGRAVITY = 1
POWERUPGRAVITYTP = 0.1
POWERUPWIDTH = 1
POWERUPHEIGHT = 1
POWERUPPROB = 0.5
SHOOTINGPADDLEACTIVETIME = 10
ENEMYHEALTH = 5


class Point:
    '''
    Defines a co-ordinate
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Dimension:
    '''
    Defines dimensions of an object in 2D world
    '''
    def __init__(self, width, height):
        self.height = height
        self.width = width