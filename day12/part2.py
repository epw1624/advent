from collections import defaultdict

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
    
def merge_boundaries(boundaries):
    merged_boundaries = {}

    for k, v in boundaries.items():
        current_boundaries = []

        v = sorted(v)

        i = 0
        while i < len(v):
            start = i

            while i + 1 < len(v) and v[i+1] == v[i] + 1:
                i += 1

            current_boundaries.append((start, i-1))
            i += 1

        merged_boundaries[k] = current_boundaries
        
    return merged_boundaries


def search(x, y, visited, plant, map):
    s = [(x, y)]
    a = 0

    # a boundary is of the form x: (y1, y2) or y: (x1, x2) where x or y represents the index of the NEXT row/column in the garden
    # x1 or y1 is the x/y value of the 'start' (upper or left end) of the boundary
    # x2 or y2 is the x/y value of the 'end' (bottom or right end) of the boundary
    x_boundaries = defaultdict(list)
    y_boundaries = defaultdict(list)

    while s:
        cx, cy = s.pop()
        if (cx, cy) not in visited:
            visited.add((cx, cy))
            a += 1

            for dx, dy in directions:
                x2, y2 = cx + dx, cy + dy
                if safe_get(x2, y2, map) == plant:
                    s.append((x2, y2))
                else:
                    if (dx, dy) == (0, -1): # top edge
                        y_boundaries[(cy, dy)].append(cx)
                    elif (dx, dy) == (1, 0):
                        x_boundaries[(cx + 1, dx)].append(cy)
                    elif (dx, dy) == (0, 1):
                        y_boundaries[(cy + 1, dy)].append(cx)
                    else:
                        x_boundaries[(cx, dx)].append(cy)

    x_boundaries = merge_boundaries(x_boundaries)
    y_boundaries = merge_boundaries(y_boundaries)

    sides = sum(len(b) for b in x_boundaries.values()) + sum(len(b) for b in y_boundaries.values())

    return a * sides



with open("day12/input.txt") as file:
    map = [line.rstrip() for line in file]

    cost = 0

    visited = set()

    for x in range(len(map[0])):
        for y in range(len(map)):
            if (x, y) not in visited:
                plant = map[y][x]
                current_cost = search(x, y, visited, plant, map)
                cost += current_cost

    print(cost)

                
    