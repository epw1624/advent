with open("input.txt") as file:
    map = [line.rstrip() for line in file]

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
    points = set()

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

    # run
    x = pos[0]
    y = pos[1]
    while x >= 0 and x < len(map[0]) and y >= 0 and y < len(map):
        if (x, y) not in points:
            points.add((x, y))

        move = directions[cur_direction]

        # next point will be off map
        if x + move[0] < 0 or x + move[0] >= len(map[0]) or y + move[1] < 0 or y + move[1] >= len(map):
            x = x + pos[0]
            y = y + pos[1]
        else:
            # if obstacle
            if map[y + move[1]][x + move[0]] == '#':
                cur_direction = turns[cur_direction]
            else:
                x = x + move[0]
                y = y + move[1]

    print(len(points))