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
            
def calculate_move(map, pos, dir):
    to_move = []
    visited = set()
    queue = [pos]
    while queue:
        curr = queue.pop(0)
        if curr not in visited:
            visited.add(curr)
            if dir == directions['^'] or dir == directions['v']:
                if map[curr[1]][curr[0]] == '[':
                    queue.append((curr[0] + 1, curr[1]))
                elif map[curr[1]][curr[0]] == ']':
                    queue.append((curr[0] - 1, curr[1]))
            next = (curr[0] + dir[0], curr[1] + dir[1])
            if map[next[1]][next[0]] == '#':
                return []
            elif map[next[1]][next[0]] in '[]':
                queue.append(next)

            to_move.append(curr)

    return to_move[::-1]

def simulate_moves(map, moves):
    x, y = find_start(map)

    for move in moves:
        direction = directions[move]
        positions_to_move = calculate_move(map, (x, y), direction)
        if positions_to_move:
            x, y = x + direction[0], y + direction[1]

            for pos in positions_to_move:
                map[pos[1] + direction[1]][pos[0] + direction[0]] = map[pos[1]][pos[0]]
                map[pos[1]][pos[0]] = '.'

    return map

def widen_map(map):
    wide_map = []
    for row in map:
        wide_row = []
        for c in row:
            if c == '#':
                wide_row.extend(['#', '#'])
            elif c == 'O':
                wide_row.extend(['[', ']'])
            elif c == '.':
                wide_row.extend(['.', '.'])
            else:
                wide_row.extend(['@', '.'])
        wide_map.append(wide_row)
    return wide_map

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    i = lines.index('')
    map = [list(line) for line in lines[:i]]
    moves = ''.join(lines[i+1:])

    map = widen_map(map)
    map = simulate_moves(map, moves)

    sum = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == '[':
                sum += 100 * y + x

    print(sum)

