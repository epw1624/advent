def analyze_row_without_dampening(row):
    increasing = int(row[1]) > int(row[0])

    for i in range(1, len(row)):
        diff = int(row[i]) - int(row[i-1])
        if increasing:
            if diff < 1 or diff > 3:
                return False
        else:
            if diff > -1 or diff < -3:
                return False
    return True

def analyze_row_with_dampening(row):
    if analyze_row_without_dampening(row):
        return True
    else:
        if analyze_row_without_dampening(row[1:]):
            return True
        elif analyze_row_without_dampening(row[:-1]):
            return True
        else:
            for i in range(1, len(row) - 1):
                if analyze_row_without_dampening(row[:i] + row[i+1:]):
                    return True
            return False

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    sum = 0

    for line in lines:
        line = line.split(" ")
        if analyze_row_with_dampening(line):
            sum = sum + 1

print(sum)



