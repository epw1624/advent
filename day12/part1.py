directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

def safe_get(x, y, map):
    if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
        return -1
    else:
        return map[y][x]

def search(x, y, visited, plant, map):
    s = [(x, y)]
    a = 0
    p = 0

    while s:
        cx, cy = s.pop()
        if (cx, cy) not in visited:
            visited.add((cx, cy))
            a += 1
            cp = 4

            for dx, dy in directions:
                x2, y2 = cx + dx, cy + dy
                if safe_get(x2, y2, map) == plant:
                    cp -= 1
                    s.append((x2, y2))

            p += cp

    return a, p



with open("input.txt") as file:
    map = [line.rstrip() for line in file]

    cost = 0

    visited = set()

    for x in range(len(map[0])):
        for y in range(len(map)):
            if (x, y) not in visited:
                plant = map[y][x]
                a, p = search(x, y, visited, plant, map)
                visited.add((x, y))
                cost += a * p

    print(cost)

                
    