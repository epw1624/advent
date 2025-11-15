BOTH = 0
PREV = 1
NEXT = 2

def main():
    sum = 0

    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]

        sum += get_line_sum("blah", lines[0], lines[1], NEXT)

        for i in range(1, len(lines) - 1):
            sum += get_line_sum(lines[i-1], lines[i], lines[i+1], BOTH)

        sum += get_line_sum(lines[-2], lines[-1], "blah", PREV)

    print(str(sum))



def find_end(line, idx):
    end = idx
    while end < len(line) and line[end].isnumeric():
        end += 1
    return end

def get_line_sum(prev_line, cur_line, next_line, mode):
    idx = 0
    sum = 0

    while idx < len(cur_line):
        if cur_line[idx].isnumeric():
            end = find_end(cur_line, idx)
            valid = False

            # cur line
            if idx > 0 and cur_line[idx-1] != '.':
                valid = True
            if end < len(cur_line) and cur_line[end] != '.':
                valid = True

            # prev line
            if mode != NEXT:
                for j in range(idx-1, end+1):
                    if j >= 0 and j < len(prev_line):
                        if prev_line[j] != '.':
                            valid = True

            # next line
            if mode != PREV:
                for j in range(idx-1, end+1):
                    if j >= 0 and j < len(next_line):
                        if next_line[j] != '.':
                            valid = True

            if valid:
                sum += int(cur_line[idx:end])

            idx = end
        else:
            idx += 1

    return sum

main()

