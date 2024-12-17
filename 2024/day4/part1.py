def safe_get(l, y, x):
    if x >= 0 and y >= 0:
        try:
            return l[y][x]
        except:
            return None
    else:
        return None

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    length = len(lines[0])

    directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

    sum = 0

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == 'X':
                for d in directions:
                    if safe_get(lines, y + d[1], x + d[0]) == 'M' and safe_get(lines, y + 2*d[1], x + 2*d[0]) == 'A' and safe_get(lines, y + 3*d[1], x+3*d[0]) == 'S':
                        sum = sum + 1

    print(sum)