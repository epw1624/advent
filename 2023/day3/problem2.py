BOTH = 0
PREV = 1
NEXT = 2

def main():
    sum = 0

    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]

        # first line
        sum += sum_line("blah", lines[0], lines[1], NEXT)

        for i in range(1, len(lines) - 1):
            sum += sum_line(lines[i-1], lines[i], lines[i+1], BOTH)

        sum += sum_line(lines[-2], lines[-1], "blah", PREV)

    print(str(sum))


def get_full_num(string, idx):
    start, end = idx, idx

    while start >= 0 and string[start].isnumeric():
        start -= 1
    start += 1

    while end < len(string) and string[end].isnumeric():
        end += 1

    return (start, end)

def sum_line(prev_line, cur_line, next_line, mode):
    sum = 0
    for i in range(len(cur_line)):
        if cur_line[i] == '*':
            nums = []
            # check cur_line
            if i > 0 and cur_line[i-1].isnumeric():
                (b, e) = get_full_num(cur_line, i-1)
                nums.append(int(cur_line[b:e]))
            if i < len(cur_line) - 1 and cur_line[i+1].isnumeric():
                (b, e) = get_full_num(cur_line, i+1)
                nums.append(int(cur_line[b:e]))
        
            if mode != NEXT:
                prev = max(i-1, 0)
                next = min(i+1, len(prev_line) - 1)
                nums += find_nums(prev_line, prev, next)

            if mode != PREV:
                prev = max(i-1, 0)
                next = min(i+1, len(next_line) - 1)
                nums += find_nums(next_line, prev, next)

            if len(nums) == 2:
                sum += nums[0]*nums[1]

    return sum


def find_nums(line, start, end):
    nums = []
    idx = start

    while idx <= end:
        if line[idx].isnumeric():
            (b, e) = get_full_num(line, idx)
            nums.append(int(line[b:e]))
            idx = e
        else:
            idx += 1
    return nums


main()        
        