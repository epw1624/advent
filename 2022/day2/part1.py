RULEBOOK = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
    'X': 'R',
    'Y': 'P',
    'Z': 'S'
}

SCOREBOOK = {
    ('R', 'R'): 4,
    ('R', 'P'): 1,
    ('R', 'S'): 7,
    ('P', 'R'): 8,
    ('P', 'P'): 5,
    ('P', 'S'): 2,
    ('S', 'R'): 3,
    ('S', 'P'): 9,
    ('S', 'S'): 6
}

with open("input.txt") as file:
    score = 0
    for line in file:
        opp, me = line.split()
        score += SCOREBOOK[(RULEBOOK[me], RULEBOOK[opp])]

    print(score)