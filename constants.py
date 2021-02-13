MAXLIFE = 3
FRAMEWIDTH = 150
FRAMEHEIGHT = 45
PADDLEWIDTH = 20
PADDLEHEIGHT = 1
PADDLESTEPX = 2
BALLSPEEDX = 1
BALLSPEEDY = 1

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