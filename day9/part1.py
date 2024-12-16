with open("input.txt") as file:
    input = [int(x) for x in file.readline()]

    # generate actual diskmap from input
    index = 0
    diskmap = []
    for i, x in enumerate(input):
        if i % 2 == 0: # file
            diskmap.extend([index] * x)
            index += 1
        else: # free space
            diskmap.extend([-1] * x)

    # compress diskmap
    p1 = 0 # index of first free space
    while diskmap[p1] != -1:
        p1 = p1 + 1

    p2 = len(diskmap) - 1 # index of last character

    while p2 > p1:
        if diskmap[p2] != -1:
            diskmap[p1], diskmap[p2] = diskmap[p2], -1
            p1 = p1 + 1
            while diskmap[p1] != -1:
                p1 = p1 + 1
        p2 = p2 - 1

    # calculate checksum
    checksum = 0
    for i, c in enumerate(diskmap):
        if c == -1:
            break
        else:
            checksum = checksum + i * int(c)

    print(checksum)