with open("day7/input.txt") as file:
    lines = [line.rstrip() for line in file]

    sum = 0

    for line in lines:
        result = int(line.split(':')[0])
        operands = [int(i) for i in line.split(':')[1].strip().split(' ')]

        result_set = {operands[0]}
        for i in range(1, len(operands)):
            result_set = {x + operands[i] for x in result_set} | {x * operands[i] for x in result_set} | {int(str(x) + str(operands[i])) for x in result_set}
        
        if result in result_set:
            sum = sum + result

    print(sum)

