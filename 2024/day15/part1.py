directions = {
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0),
        '^': (0, -1)
    }

def find_start(map):
    for x in range(len(map[0])):
        for y in range(len(map)):
            if map[y][x] == '@':
                return (x, y)

def simulate_moves(map, moves):
    x, y = find_start(map)

    for move in moves:
        n_moves = 0

        x2, y2 = x, y
        while map[y2][x2] != '.' and map[y2][x2] != '#':
            x2 = x2 + directions[move][0]
            y2 = y2 + directions[move][1]
            n_moves += 1

        if map[y2][x2] == '.': # make the move
            temp, map[y][x] = map[y][x], '.'

            for i in range(1, n_moves + 1):
                xi = x + (i * directions[move][0])
                yi = y + (i * directions[move][1])

                map[yi][xi], temp = temp, map[yi][xi]

            x, y = x + directions[move][0], y + directions[move][1] # update coordinates of '@'

    return map

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    i = lines.index('')
    map = [list(line) for line in lines[:i]]
    moves = ''.join(lines[i+1:])

    map = simulate_moves(map, moves)

    sum = 0
    for x in range(len(map[0])):
        for y in range(len(map)):
            if map[y][x] == 'O':
                sum += 100 * y + x

    print(sum)

