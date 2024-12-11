def get_result_from_operator_bitmask(i, operands):
    """
    use an integer as a bitmask for +/* operations
    # bits in i = len(operands) - 1
    """
    result = operands[0]

    for bitshift in range(len(operands) - 1):
        if (i >> bitshift) & 1:
            result = result * operands[bitshift + 1]
        else:
            result = result + operands[bitshift + 1]
    
    return result

with open("day7/input.txt") as file:
    lines = [line.rstrip() for line in file]

    sum = 0

    for line in lines:
        result = int(line.split(':')[0])
        operands = [int(i) for i in line.split(':')[1].strip().split(' ')]

        # # check if result is too small
        # min_result = get_result_from_operator_bitmask(0, operands)
        # if min_result == result:
        #     sum += result
        #     continue
        # elif min_result > result:
        #     continue

        # max_result = get_result_from_operator_bitmask(2**(len(operands)-1) - 1, operands)
        # if max_result == result:

        #     sum += result
        #     continue
        # elif max_result < result:
        #     continue

        # for i in range(1, 2**(len(operands)-1) - 1):
        for i in range(2**(len(operands)-1)):
            if get_result_from_operator_bitmask(i, operands) == result:
                sum += result
                break

    print(sum)

