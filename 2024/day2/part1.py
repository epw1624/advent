def analyze_row(row):
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

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    print(len(lines))

    sum = 0

    for line in lines:
        line = line.split(" ")
        if analyze_row(line):
            sum = sum + 1

print(sum)



