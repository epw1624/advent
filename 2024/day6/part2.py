from util.decorators import timer

directions = {
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
    '^': (0, -1)
}
turns = {
    '>': 'v',
    'v': '<',
    '<': '^',
    '^': '>'
}

def trace_path(start_pos, start_direction, map):
    pass

def detect_loop(start_pos, start_direction, map):
    x = start_pos[0]
    y = start_pos[1]
    direction = start_direction

    points = set()

    while x >= 0 and x < len(map[0]) and y >= 0 and y < len(map):
        if (direction, x, y) in points:
            return True # loop
        else:
            points.add((direction, x, y))

            move = directions[direction]
            # next point will be off map
            if x + move[0] < 0 or x + move[0] >= len(map[0]) or y + move[1] < 0 or y + move[1] >= len(map):
                return False # no loop, got off map
            else:
                # if obstacle
                if map[y + move[1]][x + move[0]] == '#':
                    direction = turns[direction]
                else:
                    x = x + move[0]
                    y = y + move[1]

def trace_path(start_pos, start_direction, map):
    """
    functionality copied from part1 because i organized this extremely poorly
    """
    points = set()

    # run
    x = start_pos[0]
    y = start_pos[1]
    direction = start_direction
    while x >= 0 and x < len(map[0]) and y >= 0 and y < len(map):
        if (x, y) not in points:
            points.add((x, y))

        move = directions[direction]

        # next point will be off map
        if x + move[0] < 0 or x + move[0] >= len(map[0]) or y + move[1] < 0 or y + move[1] >= len(map):
            x = x + start_pos[0]
            y = y + start_pos[1]
        else:
            # if obstacle
            if map[y + move[1]][x + move[0]] == '#':
                direction = turns[direction]
            else:
                x = x + move[0]
                y = y + move[1]

    return points

@timer
def task2():
    with open("day6/input.txt") as file:
        map = [line.rstrip() for line in file]

        loops = 0

        # get starting point
        cur_direction = ''
        pos = (0, 0)
        for y in range(len(map)):
            for x in range(len(map[0])):
                if map[y][x] in directions.keys():
                    cur_direction = map[y][x]
                    pos = (x, y)
                    break
            
            if cur_direction != '':
                break

        points = trace_path(pos, cur_direction, map)

        for point in points:
            if points is not pos:
                x = point[0]
                y = point[1]

                map_copy = [[x for x in y] for y in map]
                map_copy[y][x] = '#'
                if detect_loop(pos, cur_direction, map_copy):
                    loops = loops + 1

        print(loops)

if __name__ == "__main__":
    task2()