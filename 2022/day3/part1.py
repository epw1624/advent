with open("input.txt") as file:
    sum = 0
    for line in file:
        line = line.rstrip()
        c1, c2 = set(line[:len(line) // 2]), set(line[len(line) // 2:])
        common = (c1 & c2).pop()
        if ord(common) < 97:
            sum += ord(common) - 38
        else:
            sum += ord(common) - 96

    print(sum)