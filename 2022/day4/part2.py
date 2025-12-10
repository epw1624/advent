with open("input.txt") as file:
    total = 0
    lines = [line.rstrip() for line in file]
    for line in lines:
        i1, i2 = line.split(',')
        i1 = i1.split('-')
        i2 = i2.split('-')

        if not (int(i1[1]) < int(i2[0]) or int(i2[1]) < int(i1[0])):
            total += 1
    
    print(total)