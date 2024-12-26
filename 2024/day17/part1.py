with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    a = int(lines[0].split()[-1])
    b = int(lines[1].split()[-1])
    c = int(lines[2].split()[-1])

    program = lines[4].split()[-1].split(',')
    instructions = [int(x) for x in program]

    pc = 0
    output = ''

    while pc < len(instructions):
        opcode, operand = instructions[pc], instructions[pc+1]
        x = None

        # find operand
        if opcode == 0 or opcode == 2 or opcode == 5 or opcode == 6 or opcode == 7: # combo
            match operand:
                case 4: x = a
                case 5: x = b
                case 6: x = c
                case _: x = operand
        else: # literal
            x = operand

        # execute operation and update pc
        match opcode:
            case 0:
                a = int(a / 2**x)
                pc += 2
            case 1:
                b = b ^ x
                pc += 2
            case 2:
                b = x % 8
                pc += 2
            case 3:
                if a != 0:
                    pc = x
                else:
                    pc += 2
            case 4:
                b = b ^ c
                pc += 2
            case 5:
                output = output + str(x % 8) + ','
                pc += 2
            case 6:
                b = int(a / 2**x)
                pc += 2
            case _:
                c = int(a / 2**x)
                pc += 2

    print(output)

