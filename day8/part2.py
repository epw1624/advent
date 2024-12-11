with open("day8/input.txt") as file:
    map = [line.rstrip() for line in file]

    locations = set()
    antennas = {}

    # group together all points with matching frequencies
    for y in range(len(map)):
        for x in range(len(map[0])):
            l = map[y][x]
            if l != '.':
                antennas.setdefault(l, []).append((x, y))

    # go through each pair of matching-frequency points and find antinodes
    for points in antennas.values():
        for i in range(len(points)):
            pi = points[i]
            for j in range(i+1, len(points)):
                pj = points[j]
                dx = pi[0] - pj[0]
                dy = pi[1] - pj[1]

                # find all points in positive direction
                x = pi[0]
                y = pi[1]
                while x >= 0 and x < len(map[0]) and y >= 0 and y < len(map):
                    locations.add((x, y))
                    x = x + dx
                    y = y + dy

                # find all points in negative direction
                x = pj[0]
                y = pj[1]
                while x >= 0 and x < len(map[0]) and y >= 0 and y < len(map):
                    locations.add((x, y))
                    x = x - dx
                    y = y - dy

    print(len(locations))