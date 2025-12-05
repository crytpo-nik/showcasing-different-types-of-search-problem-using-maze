#this file contains the maze class and its methods


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [['0' for _ in range(width)] for _ in range(height)]
    
    def barriers(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = '1'
        else:
            raise ValueError("Coordinates out of bounds")
    
    def start_point(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 's'
        else:
            raise ValueError("Coordinates out of bounds")
    def end_point(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 'e'
        else:
            raise ValueError("Coordinates out of bounds")
    


maze1 = Maze(10, 10)
print(maze1.grid)