#this file contains the maze class and its methods
'''this module defines a Maze class that represents a maze structure with methods to add barriers,
 build the maze with random barriers, mark the path taken, track explored cells,
and visualize the maze using matplotlib, 
the probloem here is that the maze is not sophisticatede to generate a path that at the same time is solvable and contains a lot of barriers'''

import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['0' for _ in range(width)] for _ in range(height)]
        self.grid[0][0] = '-2'
        self.grid[self.width - 1][self.height - 1] = '3'

    def barrier(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = '1'
        else:
            raise ValueError("Coordinates out of bounds")
    
    def build(self, barriers_count):
        placed_barriers = 0
        while placed_barriers < barriers_count:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.grid[y][x] == '0':
                self.barrier(x, y)
                placed_barriers += 1
    def path(self, path):
        for (x, y) in path:
            if self.grid[y][x] != '-2':
                self.grid[y][x] = '3'
    def explored(self, explored):
        for (x, y) in explored:
            if self.grid[y][x] == '0' and (self.grid[y][x] != '3'):
                self.grid[y][x] = '2'


    def darw(self):

        maze_array = np.array(self.grid).astype(int)
        colors = [
            "#ff9999",  
            "#333333",    
            "#333333",    
            "#DDDDDD",
            "#FFFF00",   
            "#99ff99"  
        ]
        bounds = [-2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5]
        cmap = ListedColormap(colors)
        norm = BoundaryNorm(bounds, cmap.N)
        plt.figure(figsize=(6, 6))
        plt.imshow(maze_array, cmap=cmap, norm=norm)
        rows, cols = maze_array.shape

        plt.xticks(np.arange(-0.5, cols, 1))
        plt.yticks(np.arange(-0.5, rows, 1))

        plt.grid(color="white", linestyle="-", linewidth=0.8)

        plt.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

        plt.show()
