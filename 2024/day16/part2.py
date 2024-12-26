from heapq import heappop, heappush

directions = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
direction_order = ['N', 'E', 'S', 'W']

def find_shortest_paths(maze, sx, sy, ex, ey):
    pq = []
    heappush(pq, (0, sx, sy, 'E', set()))
    visited = set()

    paths = [[{'N': set(), 'E': set(), 'S': set(), 'W': set()} for _ in range(len(maze[0]))] for _ in range(len(maze))]
    costs = [[{'N': 2**32 - 1, 'E': 2**32 - 1, 'S': 2**32 - 1, 'W': 2**32 - 1} for _ in range(len(maze[0]))] for _ in range(len(maze))]

    while pq:
        cost, x, y, dir, path = heappop(pq)
        if (x, y, dir) in visited and cost > costs[y][x][dir]:
            continue

        visited.add((x, y, dir))
        costs[y][x][dir] = cost
        paths[y][x][dir] |= path

        # move without turning
        dx, dy = directions[dir]
        nx, ny = x + dx, y + dy
        if maze[ny][nx] != '#':
            heappush(pq, (cost + 1, nx, ny, dir, path | {(x, y)}))

        # turn in place
        di = direction_order.index(dir)

        # CCW
        ccw_dir = direction_order[(di - 1) % 4]
        heappush(pq, (cost + 1000, x, y, ccw_dir, path))

        # CW
        cw_dir = direction_order[(di + 1) % 4]
        heappush(pq, (cost + 1000, x, y, cw_dir, path))

    result = paths[ey][ex]
    return result['N'] | result['E'] | result['S'] | result['W']

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

    paths = find_shortest_paths(maze, sx, sy, ex, ey)
    print(len(paths) + 1) # add one for end tile
