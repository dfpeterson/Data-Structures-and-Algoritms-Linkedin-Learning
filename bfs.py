"""
Boilerplate code imported from the exercises
"""
from queue_ll import Queue


offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}


def read_maze(file_name):
    """
    Reads a maze stored in a text file and returns a 2d list containing the maze representation.
    """
    try:
        with open(file_name) as fh:
            maze = [[char for char in line.strip("\n")] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print("The maze is not rectangular.")
                    raise SystemExit
            return maze
    except IOError:
        print("There is a problem with the file you have selected.")
        raise SystemExit


def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze[0])
    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != "*"


def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path


def bfs(maze, start, goal):
    queue = Queue()
    queue.enqueue(start)
    predecessors = {start: None}

    while not queue.is_empty():
        current_cell = queue.dequeue()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ['up', 'right', 'down', 'left']:
            row_offset, col_offset = offsets[direction]
            neighbor = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbor) and neighbor not in predecessors:
                queue.enqueue(neighbor)
                predecessors[neighbor] = current_cell
    return None 


"""
Boilerplate code imported from the exercises"""
if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = read_maze("../../Exercise Files/06_03_begin/mazes/mini_maze_bfs.txt")
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze("../../Exercise Files/06_03_begin/mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    assert result is None
