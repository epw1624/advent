direction_encoding = {'L': 0, 'R': 1}

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    pattern = lines[0]

    map = {}

    for line in lines[2:]:
        line_items = line.split(' ')
        cur_loc = line_items[0]
        next_locs = [line_items[2].strip('(').strip(','), line_items[3].strip(')')]

        map[cur_loc] = next_locs

    index = 0
    steps = 0
    cur = 'AAA'

    while cur != 'ZZZ':
        direction = direction_encoding[pattern[index]]
        cur = map[cur][direction]
        steps += 1
        index = (index + 1) % len(pattern)

    print(steps)
