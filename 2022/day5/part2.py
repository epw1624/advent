NUM_STACKS = 9

with open("input.txt") as file:
    stacks = [[] for _ in range(NUM_STACKS)]
    lines = [line for line in file]
    newline = 0
    for i, line in enumerate(lines):
        if line == '\n':
            newline = i
            break

    stack_input = lines[:newline-1]
    procedure_input = lines[newline+1:]

    for line in stack_input:
        for col in range(NUM_STACKS):
            crate = line[4*col + 1]
            if crate != ' ':
                stacks[col] = [crate] + stacks[col]

    for proc in procedure_input:
        cnt, src, dst = int(proc.split()[1]), int(proc.split()[3]), int(proc.split()[-1])
        stack = stacks[src-1][-cnt:]
        stacks[src-1] = stacks[src-1][:len(stacks[src-1]) - cnt]
        stacks[dst-1] += stack


    result = ""
    for stack in stacks:
        result += stack[-1]

    print(result)
            
