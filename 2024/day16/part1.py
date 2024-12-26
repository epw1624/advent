from heapq import heappop, heappush

directions = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
direction_order = ['N', 'E', 'S', 'W']

def find_lowest_cost(maze, sx, sy, ex, ey):
    pq = []
    heappush(pq, (0, sx, sy, 'E'))
    visited = set()

    while pq:
        cost, x, y, dir = heappop(pq)
        if x == ex and y == ey:
            return cost
        
        if (x, y, dir) in visited:
            continue
        else:
            visited.add((x, y, dir))

        # move without turning
        dx, dy = directions[dir]
        nx, ny = x + dx, y + dy
        if maze[ny][nx] != '#':
            heappush(pq, (cost + 1, nx, ny, dir))

        # turn in place
        di = direction_order.index(dir)

        # CCW
        ccw_dir = direction_order[(di - 1) % 4]
        heappush(pq, (cost + 1000, x, y, ccw_dir))

        # CW
        cw_dir = direction_order[(di + 1) % 4]
        heappush(pq, (cost + 1000, x, y, cw_dir))

with open("input.txt") as file:
    maze = [line.rstrip() for line in file]

    # find S and E
    sx, sy = -1, -1
    ex, ey = -1, -1

    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 'S':
                sx, sy = x, y
            elif maze[y][x] == 'E':
                ex, ey = x, y

    cost = find_lowest_cost(maze, sx, sy, ex, ey)
    print(cost)
