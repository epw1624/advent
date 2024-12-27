from functools import cache

@cache
def count_design_options(d):
    if not d:
        return 1
    
    options = 0
    
    for pattern in patterns:
        if d.startswith(pattern):
            options += count_design_options(d[len(pattern):])

    return options

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    patterns = lines[0].split(', ')
    designs = lines[2:]

    possible_designs = 0
    for d in designs:
        possible_designs += count_design_options(d)

    print(possible_designs)