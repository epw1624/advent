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
            if lines[y][x] == 'A':
                if ((safe_get(lines, y-1, x-1) == 'M' and safe_get(lines, y+1, x+1) == 'S') or (safe_get(lines, y-1, x-1) == 'S' and safe_get(lines, y+1, x+1) == 'M')):
                    if ((safe_get(lines, y-1, x+1) == 'M' and safe_get(lines, y+1, x-1) == 'S') or (safe_get(lines, y-1, x+1) == 'S' and safe_get(lines, y+1, x-1) == 'M')):
                        sum = sum + 1

    print(sum)