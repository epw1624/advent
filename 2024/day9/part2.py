with open("input.txt") as file:
    input = [int(x) for x in file.readline()]

    diskmap = []
    freemap = []
    files = {}
    index = 0

    for i, x in enumerate(input):
        if i % 2 == 0: # file
            files[index] = (len(diskmap), x)
            diskmap.extend([index] * x)
            index += 1
        elif x > 0: # free space
            freemap.append((len(diskmap), x))
            diskmap.extend([0] * x)

    # compress diskmap
    for file_index in sorted(files.keys(), reverse=True):
        file_start, file_size = files[file_index]

        for free_start, free_size in freemap:
            if free_size >= file_size and free_start + free_size <= file_start: # move the file

                # move file on diskmap
                diskmap[free_start : free_start + file_size] = [file_index] * file_size
                diskmap[file_start : file_start + file_size] = [0] * file_size

                # update freemap
                freemap.remove((free_start, free_size))
                if free_size > file_size:
                    freemap.append((free_start + file_size, free_size - file_size))
                freemap.append((file_start, file_size))
                freemap = sorted(freemap)

                break

    checksum = sum(i * diskmap[i] for i in range(len(diskmap)))
    print(checksum)

