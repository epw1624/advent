with open("input.txt") as file:
    sum = 0
    lines = [line.rstrip() for line in file]
    for i in range(0, len(lines), 3):
        line_sets = [set(line) for line in lines[i:i+3]]
        common = ((line_sets[0] & line_sets[1]) & line_sets[2]).pop()
        if ord(common) < 97:
            sum += ord(common) - 38
        else:
            sum += ord(common) - 96

    print(sum)