from math import trunc
from random import randint
import time
from brick import OneUnitBrick, RainbowBrick, TwoUnitBrick, ThreeUnitBrick, UnbreakableBrick, ExplodingBrick
from constants import BRICKHEIGHT, BRICKWIDTH, Dimension, FRAMEHEIGHT, LAYOUTHEIGHT, LAYOUTWIDTH, LAYOUTXOFFSET, LAYOUTYOFFSET, Point, SHIFTDOWN, SHIFTDOWNSTARTAFTER
from frame import Frame
from arts import show_result


class LocationType:
    '''
    class for storing brick place point and it's type
    brick_type => brick
        1 => OneUnitBrick
        2 => TwoUnitBrick
        3 => ThreeUnitBrick
        4 => UnbreakableBrick
        5 => ExplodingBrick
        6 => RainbowBrick
        -1 => No brick
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
        self.total_bricks = 0
        self.point = Point(LAYOUTXOFFSET,LAYOUTYOFFSET)
        self.dimension = Dimension(LAYOUTWIDTH,LAYOUTHEIGHT)
        self.location_n_type_matrix = self.generate_location_n_type_matrix()
        self.brick_matrix = self.make_brick_matrix(self.frame)
        self.shift_down = SHIFTDOWN
        self.shift_down_after = SHIFTDOWNSTARTAFTER
        self.formed_time = time.time()
        self.lowermost = self.get_lowermost_layout_point()


    
    def get_lowermost_layout_point(self):
        '''
        This function will return the lowest point in the brick-layout
        from the remaining brick present on th screen.
        '''
        flag = False
        lowermost = self.point.y
        for row in range(len(self.brick_matrix)):
            if flag:
                break
            orow = len(self.brick_matrix)-1-row
            for cell in range(len(self.brick_matrix[orow])):
                if self.brick_matrix[orow][cell].broken == False:
                    flag = True
                    lowermost = self.brick_matrix[orow][cell].point.y + BRICKHEIGHT
                    break
        return lowermost



    def update_all_brick_location(self):
        '''
        This method will account for moving all the bricks down
        by amount=self.shift_down
        '''
        if (time.time() - self.formed_time) > self.shift_down_after:
            self.point = Point(self.point.x,self.point.y+SHIFTDOWN)
            for row in range(len(self.brick_matrix)):
                orow = len(self.brick_matrix)-1-row
                for cell in range(len(self.brick_matrix[orow])):
                    # print("Moving down")
                    self.brick_matrix[orow][cell].move_down(self.shift_down)
            print(self.get_lowermost_layout_point())
            time.sleep(2)
            if self.get_lowermost_layout_point() > (FRAMEHEIGHT-5):
                # self.frame.status.add_kill()
                show_result(self.frame.status.ret_status())
                self.frame.status.start_game()



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
                location_n_type_matrix[row].append(LocationType(Point(x_coordinate,y_coordinate),1))
                x_coordinate += cell_width
        return location_n_type_matrix
    


    def give_shape(self):
        '''
        This function will give shape to layout. And
        store it in location_n_type_matrix matrix.
        This function will get override in child class.
        '''
        pass


        
    
    def make_brick_matrix(self,frame: Frame):
        '''
        Function will place the SingleBricks at the points
        stored in the location_n_type_matrix matrix.
        '''
        self.total_bricks = 0
        brick_matrix = [ [] for j in range(len(self.location_n_type_matrix)) ]
        for row in range(len(brick_matrix)):
            for cell in range(len(self.location_n_type_matrix[row])):
                brick_point = self.location_n_type_matrix[row][cell].place_point
                brick_type = self.location_n_type_matrix[row][cell].brick_type
                self.total_bricks += 1
                if brick_type==1:
                    brick_matrix[row].append(OneUnitBrick(brick_point,frame))
                elif brick_type==2:
                    brick_matrix[row].append(TwoUnitBrick(brick_point,frame))
                elif brick_type==3:
                    brick_matrix[row].append(ThreeUnitBrick(brick_point,frame))
                elif brick_type==4:
                    brick_matrix[row].append(UnbreakableBrick(brick_point,frame))
                    self.total_bricks -= 1
                elif brick_type==5:
                    brick_matrix[row].append(ExplodingBrick(brick_point,frame))
                elif brick_type==6:
                    brick_matrix[row].append(RainbowBrick(brick_point,frame))
                else:
                    self.total_bricks -= 1
        return brick_matrix


    
    def get_brick_matrix(self):
        '''
        returns the brick matrix of the stage
        '''
        return self.brick_matrix


    
    def get_total_brick(self):
        '''
        returns the total number of bricks
        '''
        return self.total_bricks


    
    def decrease_total_brick(self):
        '''
        reduce the total number of bricks by 1
        '''
        self.total_bricks -= 1

    

    def change_rainbow_brick_color(self):
        '''
        function provides a method to change the color
        of every rainbow brick in the current layout.
        '''
        # print("here")
        # time.sleep(0.5)
        for row in range(len(self.brick_matrix)):
            for cell in range(len(self.brick_matrix[row])):
                self.brick_matrix[row][cell].change_color()



class LayoutStage2(BrickLayout):
    '''
    BrickLayout for stage
    '''
    def __init__(self,frame: Frame):
        '''
        constructor for this class
        '''
        self.frame = frame
        super().__init__(self.frame)
        self.give_shape()
        self.brick_matrix = self.make_brick_matrix(self.frame)



    def give_shape(self):
        '''
        This function is from the parrent class.
        Now overriding it to give 
        '''
        for r in range(len(self.location_n_type_matrix)):
            for c in range(len(self.location_n_type_matrix[r])):
                if r==len(self.location_n_type_matrix)-1:
                        self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,6)
                elif r==0:
                    RN = randint(1,100)%2
                    if RN==0:
                        RN=3
                    self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,RN)
                else:
                    self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,randint(2,4))
                    if (r+c)%2:
                        self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,-1)
                        self.brick_matrix[r][c].remove_brick()



class LayoutStage1(BrickLayout):
    '''
    BrickLayout for stage
    '''
    def __init__(self,frame: Frame):
        '''
        constructor for this class
        '''
        self.frame = frame
        super().__init__(self.frame)
        self.give_shape()
        self.brick_matrix = self.make_brick_matrix(self.frame)



    def give_shape(self):
        '''
        This function is from the parrent class.
        Now overriding it to give 
        '''
        for r in range(len(self.location_n_type_matrix)):
            for c in range(len(self.location_n_type_matrix[r])):
                if r==len(self.location_n_type_matrix)-1:
                        self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,randint(1,2))
                elif r==0:
                    RN = randint(1,100)%2
                    if RN==0:
                        RN=3
                    self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,RN)
                else:
                    self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,randint(2,4))
                    if (r+c)%2:
                        self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,-1)
                        self.brick_matrix[r][c].remove_brick()



class LayoutStage3(BrickLayout):
    '''
    BrickLayout for stage2
    '''
    def __init__(self,frame: Frame):
        '''
        constructor for this class
        '''
        self.frame = frame
        super().__init__(self.frame)
        self.give_shape()
        self.brick_matrix = self.make_brick_matrix(self.frame)
    


    def give_shape(self):
        '''
        This function is from the parrent class.
        Now overriding it to give 
        '''
        for r in range(len(self.location_n_type_matrix)):
            for c in range(len(self.location_n_type_matrix[r])):
                if r==len(self.location_n_type_matrix)-1:
                        self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,randint(2,4))
                elif r==2:
                        self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,randint(1,2))
                else:
                    self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,randint(1,3))
                    if (r+c)%2:
                        self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,-1)
                        self.brick_matrix[r][c].remove_brick()



class LayoutStage4(BrickLayout):
    '''
    BrickLayout for stage3
    '''
    def __init__(self,frame: Frame):
        '''
        constructor for this class
        '''
        self.frame = frame
        super().__init__(self.frame)
        self.give_shape()
        self.brick_matrix = self.make_brick_matrix(self.frame)
    


    def give_shape(self):
        '''
        This function is from the parrent class.
        Now overriding it to give 
        '''
        special_row = randint(1,len(self.location_n_type_matrix)-1)
        for r in range(len(self.location_n_type_matrix)):
            for c in range(len(self.location_n_type_matrix[r])):
                if r==special_row:
                        self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,5)
                elif r==special_row-1 or r==special_row+1:
                        self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,randint(2,4))
                else:
                    self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,randint(1,4))
                    if (r+c)%2:
                        self.location_n_type_matrix[r][c] = LocationType(self.location_n_type_matrix[r][c].place_point,-1)
                        self.brick_matrix[r][c].remove_brick()



def select_layout(stage: int,frame: Frame):
    '''
    returns the layout instance corresponding to the stage
    '''
    if stage==1:
        return LayoutStage1(frame)
    elif stage==2:
        return LayoutStage2(frame)
    elif stage==3:
        return LayoutStage3(frame)
    else:
        return LayoutStage4(frame)