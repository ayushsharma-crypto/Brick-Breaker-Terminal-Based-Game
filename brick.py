from frame import Frame
from constants import BRICKHEIGHT, BRICKWIDTH, Dimension, Point
from colorama import Fore,Back,Style


class SingleBrick:
    '''
    class for single brick
    '''
    def __init__(self,point: Point,frame: Frame):
        '''
        constructor of a single brick
        '''
        self.point = point
        self.dimension = Dimension(BRICKWIDTH,BRICKHEIGHT)
        self.shape = self.initial_shape()
        self.frame = frame




    def initial_shape(self):
        '''
        initialise shape of the single brick
        '''
        brick_row = []
        for i in range(BRICKWIDTH):
            brick_row.append(f"{Back.WHITE}{Style.DIM} {Style.RESET_ALL}")
        final_shape = []
        for i in range(BRICKHEIGHT):
            final_shape.append(brick_row)
        return final_shape




    def draw(self):
        '''
        Render ball on the base Frame Paddle
        '''
        self.frame.update_frame(self.point, self.shape, self.dimension)



    def break_brick(self):
        '''
        This will make bricks break basically clear the frame.
        '''
        self.frame.clear_frame_area(self.point,self.dimension)



class OneUnitBrick(SingleBrick):
    '''
    Bricks that will get destoyed on colliding once with the ball
    '''
    def __init__(self,point: Point,frame: Frame):
        '''
        constructor for this child class
        '''
        super().__init__(point,frame)
        self.draw()



class TwoUnitBrick(OneUnitBrick):
    '''
    Bricks that will get destoyed on colliding twice with the ball
    '''
    def __init__(self,point: Point,frame: Frame):
        '''
        constructor for this child class
        '''
        super().__init__(point,frame)
        self.shape = self.initial_shape()
        self.draw()



    def initial_shape(self):
        '''
        initialise shape of the single brick with strength two unit
        '''
        brick_row = []
        for i in range(BRICKWIDTH):
            brick_row.append(f"{Back.CYAN}{Style.BRIGHT} {Style.RESET_ALL}")
        final_shape = []
        for i in range(BRICKHEIGHT):
            final_shape.append(brick_row)
        return final_shape



class ThreeUnitBrick(TwoUnitBrick):
    '''
    Bricks that will get destoyed on colliding thrice with the ball
    '''
    def __init__(self,point: Point,frame: Frame):
        '''
        constructor for this child class
        '''
        super().__init__(point,frame)
        self.shape = self.initial_shape()
        self.draw()



    def initial_shape(self):
        '''
        initialise shape of the single brick
        '''
        brick_row = []
        for i in range(BRICKWIDTH):
            brick_row.append(f"{Back.MAGENTA}{Style.BRIGHT} {Style.RESET_ALL}")
        final_shape = []
        for i in range(BRICKHEIGHT):
            final_shape.append(brick_row)
        return final_shape



class UnbreakableBrick(SingleBrick):
    '''
    Bricks that are unbreakable but only get destroyed when collide with thru-ball
    or come together with ExplodingBrick (i.e. adjacent to them)
    '''
    def __init__(self,point: Point,frame: Frame):
        '''
        constructor for this child class
        '''
        super().__init__(point,frame)
        self.shape = self.initial_shape()
        self.draw()



    def initial_shape(self):
        '''
        initialise shape of the single brick
        '''
        brick_row = []
        for i in range(BRICKWIDTH):
            brick_row.append(f"{Back.BLACK}{Style.DIM} {Style.RESET_ALL}")
        final_shape = []
        for i in range(BRICKHEIGHT):
            final_shape.append(brick_row)
        return final_shape



class ExplodingBrick(SingleBrick):
    '''
    Special type of bricks that inhibits chain reaction.
    On colliding with ball it gets destroys along with
    other that are adjacent to it.
    '''
    def __init__(self,point: Point,frame: Frame):
        '''
        constructor for this child class
        '''
        super().__init__(point,frame)
        self.shape = self.initial_shape()
        self.draw()



    def initial_shape(self):
        '''
        initialise shape of the single brick
        '''
        brick_row = []
        for i in range(BRICKWIDTH):
            brick_row.append(f"{Back.YELLOW}{Style.BRIGHT} {Style.RESET_ALL}")
        final_shape = []
        for i in range(BRICKHEIGHT):
            final_shape.append(brick_row)
        return final_shape