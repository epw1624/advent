with open("input.txt") as file:
    content = file.read()
    counter = 3
    marker = "0000"
    for i in range(len(content)):
        counter += 1
        if len(set(content[i:i+4])) == 4:
            break

    print(counter)
