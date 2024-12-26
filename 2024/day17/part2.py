"""
To determine the correct value of A, we need to look at what the 'program' is actually doing
(and get some hints from Reddit, in my case)

My puzzle input ends with 5,5,0,3,3,0

(5, 5): OUTPUT b % 8
(0, 3): a = a / 2**3 -> equivalent to a = a >> 3
(3, 0): terminate if a is 0, else branch back to the beginning
The first instruction is the only output instruction in my puzzle input

Looking at the rest of the program:
(2, 4): b = a mod 8 -> b = a[2:0]
(1, 1): b = b XOR 1
(7, 5): c = a / 2**b
(1, 5): b = b XOR 5
(4, 3): b = b XOR c

This is good news, because the result of these operations is only dependent on a... we can ignore initial values of b and c

Because of the c = a / 2**b operation, the ith digit of the output may depend on the bits above a[3*i:3*i+3].
To account for this, I'll work through the instructions from back to front, finding the bits of a in decreasing order of significance
"""

def execute_instruction(opcode, operand, a, b, c):
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

    # execute operation
    match opcode:
        case 0:
            a = int(a / 2**x)
        case 1:
            b = b ^ x
        case 2:
            b = x % 8
        case 3:
            pass
        case 4:
            b = b ^ c
        case 5:
            output = output + str(x % 8) + ','
        case 6:
            b = int(a / 2**x)
        case _:
            c = int(a / 2**x)

    return (a, b, c)

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    program = lines[4].split()[-1].split(',')
    instructions = [int(x) for x in program]

    possible_a_values = [0]
    for x in reversed(instructions):
        new_a_values = []
        for a in possible_a_values:
            for ra_lsb in range(8):
                ra = 8 * a + ra_lsb
                rb, rc = 0, 0
                for pc in range(0, 10, 2): # 10 is the output instruction... if I wasn't lazy I would have avoided hard coding it
                    ra, rb, rc = execute_instruction(instructions[pc], instructions[pc + 1], ra, rb, rc)
                
                if rb % 8 == x:
                    new_a_values.append(8 * a + ra_lsb)

        possible_a_values = new_a_values

    print(min(possible_a_values))

