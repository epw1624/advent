from heapq import heappop, heappush

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def shortest_path(grid, sx, sy, ex, ey):
    pq = []
    heappush(pq, (0, sx, sy))
    visited = set()

    while pq:
        l, x, y = heappop(pq)
        if x == ex and y == ey:
            return l
        
        if (x, y) in visited:
            continue
        else:
            visited.add((x, y))

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < len(grid[0]) and ny >= 0 and ny < len(grid) and grid[ny][nx] != '#':
                heappush(pq, (l + 1, nx, ny))

with open("input.txt") as file:
    grid = [list(line.rstrip()) for line in file]

    # find S and E
    sx, sy = -1, -1
    ex, ey = -1, -1

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                sx, sy = x, y
            elif grid[y][x] == 'E':
                ex, ey = x, y

    # find original shortest path
    original_path = shortest_path(grid, sx, sy, ex, ey)

    path_count = 0
    for x in range(1, len(grid[0]) - 1):
        for y in range(1, len(grid) - 1):
            if grid[y][x] == '#':
                grid[y][x] = '.'
                path = shortest_path(grid, sx, sy, ex, ey)
                grid[y][x] = '#'

                if original_path - path >= 100:
                    path_count += 1

    print(path_count)
