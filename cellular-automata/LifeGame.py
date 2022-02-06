from manim import *
import random
import time

# TODO, Add borders
class CellTable(VGroup):
    """Create a table of cells for the game of life

    Parameters
    ----------
    colors : Colors of the cells
    The color is by default WHITE in an activated cell, and GREY in a terminated cell

    shape: The size of the table (must be square)
    base 0

    shape_sets (Settings of the table):
    block_width, width_buff_ratio, buff

    activation_function: rules of the game
    To let the current cell become activated, 
    the range of activated adjacent cells is by default [2, 3]
    
    To let the current space become activated,
    the range of activated adjacent cells is by default [3, 3]

    active_probability: used in random stage
    When the probability is larger,  there would be more active cells in the table

    original_stage_set: The original stage, if it is not set by the user,
    then a random stage will be generated

    random_seed: seed for generating random stage
    """
    def __init__(self, colors = {'activated': WHITE, 'terminated': GREY,}, 
                    shape = (10, 10), shape_sets = {'block_width': 0.6, 'width_buff_ratio': 6.0, 'buff': None,},
                    activation_function = {'min_neighbor_for_activation': 2, 'max_neighbor_for_activation': 3,
                                            'min_neighbor_for_reproduction': 3, 'max_neighbor_for_reproduction': 3},
                    active_probability = 0.05, original_stage_set = None, random_seed = None,
                    **kwargs):

        VGroup.__init__(self, **kwargs)

        self.colors = colors 
        self.shape = shape
        self.shape_sets = shape_sets
        self.activation_function = activation_function
        self.active_probability = active_probability
        self.original_stage_set = original_stage_set
        self.random_seed = random_seed

        if not self.random_seed:
            self.random_seed = time.time()*10000
        random.seed(self.random_seed)

        if self.original_stage_set is None:
            self.stage = np.zeros((self.shape)).T
        else:
            self.stage = self.original_stage_set.T
        
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                if self.original_stage_set is None:
                    self.stage[x, y] = self.get_random_stage()
                self.add(
                    Square(side_length=self.shape_sets['block_width'], color=self.stage_to_color(self.stage[x, y]), fill_opacity=1)\
                        .move_to(self.get_position(x, y))
                )

    def __getitem__(self, index):
        # Inside, row / col inverted
        flat = index[1] + self.shape[1] * index[0]
        return VGroup.__getitem__(self, int(flat))

    def get_square(self, index):
        flat = index[0] + self.shape[0] * index[1]
        return VGroup.__getitem__(self, int(flat))

    def stage_to_color(self, stage):
        if stage:
            return self.colors['activated']
        else:
            return self.colors['terminated']

    def get_random_stage(self):
        rand = random.uniform(0, 1)
        if rand < self.active_probability:
            return 1
        else:
            return 0

    def get_position(self, column, row):
        if self.shape_sets['buff'] == None:
            self.shape_sets['buff'] = self.shape_sets['block_width']/self.shape_sets['width_buff_ratio']
        return np.array([
            (self.shape_sets['block_width']+self.shape_sets['buff'])*(column-self.shape[0]/2)+self.shape_sets['buff'],
            (self.shape_sets['block_width']+self.shape_sets['buff'])*(self.shape[1]/2-row)+self.shape_sets['buff'],
            0,
        ])

    def get_activated_vgroup(self):
        tmp = VGroup()
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                if self.stage[x, y]:
                    tmp += self.__getitem__([x, y])
        return tmp

    def get_terminated_vgroup(self):
        tmp = VGroup()
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                if not self.stage[x, y]:
                    tmp += self.__getitem__([x, y])
        return tmp

    def get_surrounded_vgroup(self, index):
        index[0], index[1] = index[1], index[0]
        tmp = VGroup()
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue
                if index[0] + x < 0 or index[0] + x >= self.shape[0]:
                    continue
                if index[1] + y < 0 or index[1] + y >= self.shape[1]:
                    continue
                tmp += self.__getitem__([index[0] + x, index[1] + y])
        return tmp
    
    # x is column, y is row
    def count_neighbor(self, x, y):
        neighbor = 0
        location = np.array([x, y])
        directions = np.array([RIGHT, UR, UP, UL, LEFT, DL, DOWN, DR])[:,:2].astype(np.int8)
        for direction in directions:
            detect = location + direction
            if detect[0] >= 0 and detect[0] < self.shape[0] and detect[1] >= 0 and detect[1] < self.shape[1]:
                if self.stage[tuple(detect)]:
                    neighbor += 1 
        return neighbor

    def activation_func(self, x, y):
        neighbor = self.count_neighbor(x, y)
        if self.stage[x][y]: #  current place is cell
            if neighbor >= self.activation_function['min_neighbor_for_activation'] and neighbor <= self.activation_function['max_neighbor_for_activation']:
                return 1
            else:
                return 0
        else: # current place is space
            if neighbor >= self.activation_function['min_neighbor_for_reproduction'] and neighbor <= self.activation_function['max_neighbor_for_reproduction']:
                return 1
            else:
                return 0


    def count(self):
        acti = term = 0
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                if self.stage[x, y]:
                    acti += 1
                else:
                    term += 1
        return (acti, term)

    def step(self):
        new_stage = np.array([[self.activation_func(x, y) for y in range(self.shape[1])]for x in range(self.shape[0])])
        for x in range(self.shape[0]):
            for y in range(self.shape[1]):
                if self.stage[x, y] != new_stage[x, y]:
                    self.stage[x, y] = new_stage[x, y]
                    self[x, y].set_color(self.stage_to_color(self.stage[x, y]))
