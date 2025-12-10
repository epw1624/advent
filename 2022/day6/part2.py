with open("input.txt") as file:
    content = file.read()
    counter = 13
    for i in range(len(content)):
        counter += 1
        if len(set(content[i:i+14])) == 14:
            break

    print(counter)
