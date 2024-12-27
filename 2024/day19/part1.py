from functools import cache

@cache
def is_design_possible(d):
    if not d or d in patterns:
        return True
    
    for i in range(1, len(d)):
        if is_design_possible(d[:i]) and is_design_possible(d[i:]):
            return True
        
    return False

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    patterns = lines[0].split(', ')
    designs = lines[2:]

    possible_designs = 0
    for d in designs:
        if is_design_possible(d):
            possible_designs += 1

    print(possible_designs)