from heapq import heappop, heappush

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
CHEAT_THRESHOLD = 100

def shortest_path(grid, sx, sy, ex, ey):
    pq = []
    heappush(pq, (0, sx, sy, []))
    visited = set()

    while pq:
        l, x, y, path = heappop(pq)
        if x == ex and y == ey:
            return l, path + [(ex, ey)]
        
        if (x, y) in visited:
            continue
        else:
            visited.add((x, y))

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < len(grid[0]) and ny >= 0 and ny < len(grid) and grid[ny][nx] != '#':
                heappush(pq, (l + 1, nx, ny, path + [(x, y)]))

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
    original_length, original_path = shortest_path(grid, sx, sy, ex, ey)

    cheats = 0

    for i in range(original_length + 1):
        for j in range(i + 1, original_length + 1):
            pix, piy, pjx, pjy = original_path[i][0], original_path[i][1], original_path[j][0], original_path[j][1]
            dist = abs(pix - pjx) + abs(piy - pjy)
            if dist <= 20:
                cheat = i + dist + (original_length - j)
                diff = original_length - cheat
                if diff >= CHEAT_THRESHOLD:
                    cheats += 1


    print(cheats)