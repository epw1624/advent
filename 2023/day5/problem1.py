def main():

    min_loc = -1

    data, temp = get_data_from_file("input.txt")
    nums = []
    for num in temp:
        nums.append(int(num))

    for num in nums:
        for step in data:
            for interval in step:
                if num >= interval[1] and num < interval[1] + interval[2]:
                    num += (interval[0] - interval[1])
                    break

        if min_loc == -1:
            min_loc = num
        else:
            min_loc = min(num, min_loc)

    print(min_loc)


def get_data_from_file(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    data = []
    cur_set = []
    targets = lines[0].split(' ')[1:]

    for i in range(2, len(lines)):
        if lines[i] == "":
            data.append(cur_set)
        elif not lines[i][0].isnumeric():
            cur_set = []
        else:
            dest, source, interval = lines[i].split(' ')
            cur_set.append([int(dest), int(source), int(interval)])

    data.append(cur_set)
    return data, targets

main()

            

