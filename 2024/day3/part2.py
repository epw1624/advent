import re

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    pattern = "mul\(\d+,\d+\)|do\(\)|don't\(\)"
    sum = 0
    enabled = True

    for line in lines:
        operations = re.findall(pattern, line)

        for o in operations:
            if o == "do()":
                enabled = True
            elif o == "don't()":
                enabled = False
            elif enabled:
                m1 = int(o.split('(')[1].split(',')[0])
                m2 = int(o.split(',')[1].split(')')[0])
                sum += m1 * m2

    print(sum)

