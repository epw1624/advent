from functools import cache

DEPTH = 2

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
    [None, '0', 'A']
]

DIRECTIONAL_KEYPAD = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]

NUMERIC_PATHS = {}
DIRECTIONAL_PATHS = {}

# Keypad shortest path functions
def find_all_paths():
    numeric_paths, directional_paths = {}, {}

    for s, (x1, y1) in NUMERIC.items():
        for e, (x2, y2) in NUMERIC.items():
            path = ''
            if x2 > x1:
                path += '>' * (x2 - x1)
            if y2 < y1:
                path += '^' * abs(y2 - y1)
            if y2 > y1:
                path += 'v' * (y2 - y1)
            if x2 < x1:
                path += '<' * abs(x2 - x1)

            numeric_paths[(s, e)] = path

    for s, (x1, y1) in DIRECTIONAL.items():
        for e, (x2, y2) in DIRECTIONAL.items():
            path = ''
            if x2 > x1:
                path += '>' * (x2 - x1)
            if y2 > y1:
                path += 'v' * (y2 - y1)
            if y2 < y1:
                path += '^' * abs(y2 - y1)
            if x2 < x1:
                path += '<' * abs(x2 - x1)
            
            directional_paths[(s, e)] = path

    return numeric_paths, directional_paths
    
# Code-finding functions
@cache
def get_next_code(code, numeric):
    new_code = ""

    for i, c in enumerate(code):
        prev = 'A' if i == 0 else code[i-1]

        if numeric:
            next = NUMERIC_PATHS[(prev, c)]
        else:
            next = DIRECTIONAL_PATHS[(prev, c)]

        new_code = new_code + next + 'A'
        
    print(new_code)
    return new_code

def get_codes(code, depth):
    next_code = get_next_code(code, numeric=(depth==DEPTH))
    if depth == 0:
        return len(next_code)
    else:
        return get_codes(next_code, depth - 1)
    

with open("input.txt") as file:
    input = [line.rstrip() for line in file]

    NUMERIC_PATHS, DIRECTIONAL_PATHS = find_all_paths()

    complexity = 0
    for line in input:
        length = get_codes(line, DEPTH)
        print(length, int(line[:-1]))
        complexity += length * int(line[:-1])

    print(complexity)
