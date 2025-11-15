import math

direction_encoding = {'L': 0, 'R': 1}

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    pattern = lines[0]

    map = {}
    cur_locs = []

    for line in lines[2:]:
        line_items = line.split(' ')
        cur_loc = line_items[0]
        next_locs = [line_items[2].strip('(').strip(','), line_items[3].strip(')')]

        map[cur_loc] = next_locs
        if cur_loc[-1] == 'A':
            cur_locs.append(cur_loc)

    num_steps = []

    for loc in cur_locs:
        steps = 0
        index = 0
        while loc[-1] != 'Z':
            direction = direction_encoding[pattern[index]]
            loc = map[loc][direction]
            steps += 1
            index = (index + 1) % len(pattern)

        num_steps.append(steps)

    lcm = 1
    for num in num_steps:
        lcm = math.lcm(lcm, num)


    print(lcm)




