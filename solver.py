from maze import Maze
from collections import deque

maze1 = Maze(10, 10)
maze1.build(30)

def bfs(maze):
    start = (0, 0)
    goal = (maze.width - 1, maze.height - 1)
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            maze.path(path)
            return path

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if (0 <= neighbor[0] < maze.width and
                0 <= neighbor[1] < maze.height and
                maze.grid[neighbor[1]][neighbor[0]] != '1' and
                neighbor not in visited):
                
                queue.append(neighbor)
                visited.add(neighbor)
                maze.explored(visited)
                parent[neighbor] = current

    return None

def dfs(maze):
    start = (0, 0)
    goal = (maze.width - 1, maze.height - 1)
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        current = queue.pop()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            maze.path(path)
            return path

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])

            if (0 <= neighbor[0] < maze.width and
                0 <= neighbor[1] < maze.height and
                maze.grid[neighbor[1]][neighbor[0]] != '1' and
                neighbor not in visited):
                
                queue.append(neighbor)
                visited.add(neighbor)
                maze.explored(visited)
                parent[neighbor] = current

    return None
