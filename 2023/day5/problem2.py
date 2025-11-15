def main():
    data, targets = get_data_from_file("input.txt")

    loc = 46

    while True:
        temp = loc

        for step in data:
            for interval in step:
                if temp >= interval[0] and temp < interval[0] + interval[2]:
                    temp -= (interval[0] - interval[1])
                    break

        for valid_range in targets:
            if temp >= valid_range[0] and temp < valid_range[0] + valid_range[1]:
                return loc
            
        loc += 1



def get_data_from_file(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    data = []
    cur_set = []
    nums = lines[0].split(' ')[1:]
    targets = []

    for i in range(0, len(nums), 2):
        targets.append([int(nums[i]), int(nums[i+1])])

    for i in range(2, len(lines)):
        if lines[i] == "":
            data.append(cur_set)
        elif not lines[i][0].isnumeric():
            cur_set = []
        else:
            dest, source, interval = lines[i].split(' ')
            cur_set.append([int(dest), int(source), int(interval)])

    data.append(cur_set)
    data.reverse()
    return data, targets

print(main())