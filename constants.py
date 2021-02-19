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
BRICKWIDTH = 3
BRICKHEIGHT = 2
LAYOUTWIDTH = 80
LAYOUTHEIGHT = 10
LAYOUTXOFFSET = 35
LAYOUTYOFFSET = 6

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