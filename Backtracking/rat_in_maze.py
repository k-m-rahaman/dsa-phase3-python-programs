def solveMaze(maze, x, y, path, res, n):
    if x == n-1 and y == n-1:
        res.append(path)
        return

    if x < 0 or y < 0 or x >= n or y >= n or maze[x][y] == 0:
        return

    maze[x][y] = 0

    solveMaze(maze, x+1, y, path+"D", res, n)
    solveMaze(maze, x, y+1, path+"R", res, n)
    solveMaze(maze, x-1, y, path+"U", res, n)
    solveMaze(maze, x, y-1, path+"L", res, n)

    maze[x][y] = 1


def ratMaze(maze, n):
    res = []
    solveMaze(maze, 0, 0, "", res, n)
    return res


maze = [
    [1,0,0,0],
    [1,1,0,1],
    [0,1,0,0],
    [1,1,1,1]
]

print(ratMaze(maze, 4))