from heapq import heappop, heappush

GRID_SIZE=71
BYTES_TO_SIMULATE=1024
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def shortest_path(grid):
    pq = []
    heappush(pq, (0, 0, 0))
    visited = set()

    while pq:
        l, x, y = heappop(pq)
        if x == GRID_SIZE - 1 and y == GRID_SIZE - 1:
            return l
        
        if (x, y) in visited:
            continue
        else:
            visited.add((x, y))

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < GRID_SIZE and ny >= 0 and ny < GRID_SIZE and grid[ny][nx] != '#':
                heappush(pq, (l + 1, nx, ny))

with open("input.txt") as file:
    bytes = [line.rstrip() for line in file]

    # initialize empty grid
    grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # simulate bytes falling
    for i in range(BYTES_TO_SIMULATE):
        byte = bytes[i].split(',')
        x, y = int(byte[0]), int(byte[1])
        grid[y][x] = '#'

    # find shortest path
    path = shortest_path(grid)
    print(path)
