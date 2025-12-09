CODEBOOK = {
    'A': 'R',
    'B': 'P',
    'C': 'S',
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

RULEBOOK = {
    ('R', 'X'): 'S',
    ('R', 'Y'): 'R',
    ('R', 'Z'): 'P',
    ('P', 'X'): 'R',
    ('P', 'Y'): 'P',
    ('P', 'Z'): 'S',
    ('S', 'X'): 'P',
    ('S', 'Y'): 'S',
    ('S', 'Z'): 'R'
}

with open("input.txt") as file:
    score = 0
    for line in file:
        opp, outcome = line.split()
        opp = CODEBOOK[opp]
        score += SCOREBOOK[(RULEBOOK[(opp, outcome)], opp)]

    print(score)