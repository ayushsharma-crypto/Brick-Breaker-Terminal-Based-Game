import time as tm

from frame import Frame
from constants import BASICSCOREINCREMENT, BRICKHEIGHT, BRICKWIDTH, Dimension, Point
from colorama import Fore,Back,Style

BRICK_TYPE_ARRAY = [
    f"{Back.WHITE}{Style.DIM} {Style.RESET_ALL}",
    f"{Back.CYAN}{Style.BRIGHT} {Style.RESET_ALL}",
    f"{Back.MAGENTA}{Style.BRIGHT} {Style.RESET_ALL}",
    f"{Back.BLACK}{Style.DIM} {Style.RESET_ALL}",
    f"{Back.YELLOW}{Style.BRIGHT} {Style.RESET_ALL}"
]

class SingleBrick:
    '''
    class for single brick
    '''
    def __init__(self,point: Point,frame: Frame):
        '''
        constructor of a single brick
        '''
        self.break_brick_time = 1
        self.point = point
        self.dimension = Dimension(BRICKWIDTH,BRICKHEIGHT)
        self.shape = self.initial_shape(Back.WHITE,Style.DIM)
        self.frame = frame




    def initial_shape(self,color,style):
        '''
        initialise shape of the single brick
        '''
        brick_row = []
        for i in range(BRICKWIDTH):
            brick_row.append(f"{color}{style} {Style.RESET_ALL}")
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
        if self.break_brick_time>0:
            self.break_brick_time -= 1
            self.frame.clear_frame_area(self.point,self.dimension)
            self.frame.status.add_score(BASICSCOREINCREMENT)



    def remove_brick(self):
        '''
        This will remove the bricks.
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
        self.break_brick_time = 2
        self.shape = self.initial_shape(Back.CYAN,Style.BRIGHT)
        self.draw()



    def break_brick(self):
        '''
        This will make bricks break basically clear the frame.
        '''
        if self.break_brick_time==2:
            self.break_brick_time -= 1
            self.shape = self.initial_shape(Back.WHITE,Style.DIM)
            self.draw()
        elif self.break_brick_time==1:
            self.break_brick_time -= 1
            self.frame.clear_frame_area(self.point,self.dimension)
            self.frame.status.add_score(BASICSCOREINCREMENT)



class ThreeUnitBrick(OneUnitBrick):
    '''
    Bricks that will get destoyed on colliding thrice with the ball
    '''
    def __init__(self,point: Point,frame: Frame):
        '''
        constructor for this child class
        '''
        super().__init__(point,frame)
        self.break_brick_time=3
        self.shape = self.initial_shape(Back.MAGENTA,Style.BRIGHT)
        self.draw()



    def break_brick(self):
        '''
        This will make bricks break basically clear the frame.
        '''
        if self.break_brick_time==3:
            self.break_brick_time -= 1
            self.shape = self.initial_shape(Back.CYAN,Style.BRIGHT)
            self.draw()

        elif self.break_brick_time==2:
            self.break_brick_time -= 1
            self.shape = self.initial_shape(Back.WHITE,Style.DIM)
            self.draw()

        elif self.break_brick_time==1:
            self.break_brick_time -= 1
            self.frame.clear_frame_area(self.point,self.dimension)
            self.frame.status.add_score(BASICSCOREINCREMENT)



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
        self.shape = self.initial_shape(Back.BLACK,Style.DIM)
        self.draw()



    def break_brick(self):
        '''
        This will make bricks break basically clear the frame.
        '''
        self.frame.clear_frame_area(self.point,self.dimension)
        self.shape = self.initial_shape(Back.BLACK,Style.DIM)
        self.draw()



    def explode_unbreak_brick(self):
        '''
        This will make bricks break basically clear the frame when
        exploded due to chain reaction.
        '''
        self.break_brick_time = 0
        self.frame.clear_frame_area(self.point,self.dimension)



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
        self.shape = self.initial_shape(Back.YELLOW,Style.BRIGHT)
        self.draw()