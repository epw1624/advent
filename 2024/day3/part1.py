import re

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    pattern = 'mul\(\d+,\d+\)'
    sum = 0

    for line in lines:
        operations = re.findall(pattern, line)

        for o in operations:
            m1 = int(o.split('(')[1].split(',')[0])
            m2 = int(o.split(',')[1].split(')')[0])

            sum += m1 * m2

    print(sum)

