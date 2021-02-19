from random import randint
from brick import OneUnitBrick, TwoUnitBrick, ThreeUnitBrick, UnbreakableBrick, ExplodingBrick
from constants import BRICKHEIGHT, BRICKWIDTH, Dimension, LAYOUTHEIGHT, LAYOUTWIDTH, LAYOUTXOFFSET, LAYOUTYOFFSET, Point
from frame import Frame



class LocationType:
    '''
    class for storing brick place point and it's type
    brick_type => brick
    1 => OneUnitBrick
    2 => TwoUnitBrick
    3 => ThreeUnitBrick
    4 => UnbreakableBrick
    5 => ExplodingBrick
    '''
    def __init__(self,place_point: Point,brick_type: int=1):
        self.place_point = place_point
        self.brick_type = brick_type



class BrickLayout:
    '''
    Brick Layout parent class for level/stage of the player.
    Right now it is default layout.
    '''
    def __init__(self, frame: Frame):
        '''
        constructor of the brick layout
        '''
        self.frame = frame
        self.point = Point(LAYOUTXOFFSET,LAYOUTYOFFSET)
        self.dimension = Dimension(LAYOUTWIDTH,LAYOUTHEIGHT)
        self.location_n_type_matrix = self.generate_location_n_type_matrix()
        self.brick_matrix = self.make_brick_matrix(self.frame)
    


    def generate_location_n_type_matrix(self):
        '''
        This function will generate a matrix of points i.e. (x,y)
        which will be used to place the SingleBricks.And store it
        in location_n_type_matrix matrix.
        '''
        row_height = BRICKHEIGHT+1
        cell_width = BRICKWIDTH+1
        location_n_type_matrix = [ [] for j in range((self.dimension.height)//(row_height)) ]
        for row in range(len(location_n_type_matrix)):
            y_coordinate = self.point.y+(row*(row_height))
            x_coordinate = self.point.x
            while x_coordinate <= (self.point.x+self.dimension.width-cell_width):
                brick_type = randint(1,5)
                location_n_type_matrix[row].append(LocationType(Point(x_coordinate,y_coordinate),brick_type))
                x_coordinate += cell_width
        return location_n_type_matrix


        
    
    def make_brick_matrix(self,frame: Frame):
        '''
        Function will place the SingleBricks at the points
        stored in the location_n_type_matrix matrix.
        '''
        brick_matrix = [ [] for j in range(len(self.location_n_type_matrix)) ]
        for row in range(len(brick_matrix)):
            for cell in range(len(self.location_n_type_matrix[row])):
                brick_point = self.location_n_type_matrix[row][cell].place_point
                brick_type = self.location_n_type_matrix[row][cell].brick_type
                if brick_type==1:
                    brick_matrix[row].append(OneUnitBrick(brick_point,frame))
                elif brick_type==2:
                    brick_matrix[row].append(TwoUnitBrick(brick_point,frame))
                elif brick_type==3:
                    brick_matrix[row].append(ThreeUnitBrick(brick_point,frame))
                elif brick_type==4:
                    brick_matrix[row].append(UnbreakableBrick(brick_point,frame))
                elif brick_type==5:
                    brick_matrix[row].append(ExplodingBrick(brick_point,frame))
        return brick_matrix


    
    def get_brick_matrix(self):
        '''
        returns the brick matrix of the stage
        '''
        return self.brick_matrix