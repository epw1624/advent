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

                p1 = (pi[0] + dx, pi[1] + dy)
                if p1[0] >= 0 and p1[0] < len(map[0]) and p1[1] >= 0 and p1[1] < len(map):
                    locations.add(p1)

                p2 = (pj[0] - dx, pj[1] - dy)
                if p2[0] >= 0 and p2[0] < len(map[0]) and p2[1] >= 0 and p2[1] < len(map):
                    locations.add(p2)

    print(len(locations))