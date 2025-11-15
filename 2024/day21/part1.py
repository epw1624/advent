from heapq import heappop, heappush

LAYERS = 3

DIRECTIONS = {
    (1, 0): '>', 
    (0, 1): 'v', 
    (-1, 0): '<', 
    (0, -1): '^'
}

NUMERIC = {
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    '0': (1, 3),
    'A': (2, 3)
}

DIRECTIONAL = {
    '^': (1, 0),
    'A': (2, 0),
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1)
}

NUMERIC_KEYPAD = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['.', '0', 'A']
]

DIRECTIONAL_KEYPAD = [
    ['.', '^', 'A'],
    ['<', 'v', '>']
]

def find_paths(keypad, sx, sy, ex, ey):
    pq = []
    heappush(pq, (0, sx, sy, ""))

    paths = [[(5, set()) for _ in range(len(keypad[0]))] for _ in range(len(keypad))]

    while pq:
        l, x, y, path = heappop(pq)
        if l > paths[y][x][0] or path in paths[y][x][1]:
            continue

        paths[y][x] = (len(path), paths[y][x][1] | {path})

        for d, c in DIRECTIONS.items():
            dx, dy = d
            x2, y2 = x + dx, y + dy
            if x2 >= 0 and x2 < len(keypad[0]) and y2 >= 0 and y2 < len(keypad) and keypad[y][x] != '.':
                heappush(pq, (l + 1, x2, y2, path + c))

    return paths[ey][ex][1]

def get_parent_codes(code, numeric):
    codes = ['']

    if numeric:
        keypad = NUMERIC_KEYPAD
        button_mappings = NUMERIC
    else:
        keypad = DIRECTIONAL_KEYPAD
        button_mappings = DIRECTIONAL

    for i, c in enumerate(code):
        if i == 0:
            prev = 'A'
        else:
            prev = code[i-1]
        
        sx, sy = button_mappings[prev]
        ex, ey = button_mappings[c]

        next_codes = find_paths(keypad, sx, sy, ex, ey)
        updated_codes = set()
        for c in codes:
            for n in next_codes:
                updated_codes.add(c + n + 'A')
        codes = updated_codes

    print(list(codes)[0])
    return list(codes)

with open("input.txt") as file:
    input = [line.rstrip() for line in file]

    complexity = 0
    for line in input:
        codes = [line]
        for i in range(LAYERS):
            new_codes = []
            for code in codes:
                parent_codes = get_parent_codes(code, i == 0)
                if not new_codes or len(parent_codes[0]) < len(new_codes[0]):
                    new_codes = parent_codes
                elif len(parent_codes[0]) == len(new_codes[0]):
                    new_codes.extend(parent_codes)
            codes = new_codes

        complexity += len(codes[0]) * int(line[:-1])

    print(complexity)
