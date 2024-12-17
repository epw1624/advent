memo = []

def safe_get(x, y, map):
    if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map):
        return -1
    else:
        return map[y][x]

def valid_trails(x, y, map):
    if safe_get(x, y, map) == -1: # base case 1: off map
        return set()
    
    if memo[y][x] == -1:
        start = map[y][x]

        if start == 9: # base case 2: end of trail
            memo[y][x] = {(x, y)}
        else:
            trails = set()
            if safe_get(x, y-1, map) == start + 1:
                trails = trails | valid_trails(x, y-1, map)
            if safe_get(x+1, y, map) == start + 1:
                trails = trails | valid_trails(x+1, y, map)
            if safe_get(x, y+1, map) == start + 1:
                trails = trails | valid_trails(x, y+1, map)
            if safe_get(x-1, y, map) == start + 1:
                trails = trails | valid_trails(x-1, y, map)
            
            memo[y][x] = trails

    return memo[y][x]

with open("input.txt") as file:
    map = [list(map(int, line.rstrip())) for line in file]

    memo = [[-1 for x in map[0]] for y in map]

    trails = 0

    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 0:
                trails += len(valid_trails(x, y, map))

    print(trails)
