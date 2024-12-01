with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    first_col = [l.split(" ")[0] for l in lines]
    second_col = [l.split(" ")[-1] for l in lines]

    second_col_frequencies = {}

    total = 0

    for num in second_col:
        second_col_frequencies[num] = second_col_frequencies.get(num, 0) + 1

    for num in first_col:
        frequency = second_col_frequencies.get(num, 0)
        total += int(num) * int(frequency)

    print(total)

    