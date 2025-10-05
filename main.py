# Path-Finder-in-a-Maze-using-BFS.
def read_maze(filename):
    maze = []
    start = end = None
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            row = list(line.strip())
            for j, cell in enumerate(row):
                if cell == 'S':
                    start = (i, j)
                elif cell == 'E':
                    end = (i, j)
            maze.append(row)
    return maze, start, end

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = [start]
    visited = set()
    visited.add(start)
    parent = {start: None}

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        current = queue.pop(0)
        if current == end:
            break
        for dx, dy in directions:
            ni, nj = current[0] + dx, current[1] + dy
            if 0 <= ni < rows and 0 <= nj < cols:
                if maze[ni][nj] != '1' and (ni, nj) not in visited:
                    queue.append((ni, nj))
                    visited.add((ni, nj))
                    parent[(ni, nj)] = current
    return parent

def mark_path(maze, start, end, parent):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent.get(current)
        if current is None:
            print("No path found.")
            return
    path.reverse()
    for i, j in path:
        if maze[i][j] not in ('S', 'E'):
            maze[i][j] = '*'

def print_maze(maze):
    for row in maze:
        print("".join(row))

def main():
    print("✅ Program started...")

    maze, start, end = read_maze("maze.txt")

    if not maze:
        print("❌ Error: Maze is empty.")
        return
    if start is None or end is None:
        print("❌ Error: Maze must contain both 'S' (start) and 'E' (end).")
        return

    parent = bfs(maze, start, end)
    if end in parent:
        mark_path(maze, start, end, parent)
        print("✅ Shortest path marked with '*':\n")
        print_maze(maze)
    else:
        print("❌ No path found from Start to End. Maze might be blocked.")
        print("\nMaze layout:")
        print_maze(maze)

if __name__ == "__main__":
    main()
