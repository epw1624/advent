with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    first_col = [l.split(" ")[0] for l in lines]
    second_col = [l.split(" ")[-1] for l in lines]

    first_col.sort()
    second_col.sort()

    total = 0

    for i in range(len(first_col)):
        total += abs(int(first_col[i]) - int(second_col[i]))

    print(total)