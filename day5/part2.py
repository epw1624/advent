def fix_print(p, rules):
    n = len(p)
    
    streak = 0
    while streak == 0:
        swapped = False
        for i in range(n):
            for j in range(i + 1, n):
                if p[j] in rules.get(p[i], []):
                    p[i], p[j] = p[j], p[i]
                    swapped = True
        if not swapped:
            streak = streak + 1

    return p

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    sum = 0

    divider = lines.index('')
    rules = lines[:divider]
    prints = lines[divider+1:]

    rule_map = {}

    for rule in rules:
        k, v = rule.split('|')

        if v in rule_map.keys():
            rule_map[v].append(k)
        else:
            rule_map[v] = [k]

    for p in prints:
        p = p.split(',')

        n = len(p)
        valid = True

        for i in range(n):
            for j in range(i + 1, n):
                if p[j] in rule_map.get(p[i], []):
                    valid = False
                    break
            if not valid:
                break
        
        if not valid:
            p = fix_print(p, rule_map)
            sum = sum + int(p[int(n/2)])

    print(sum)