with open("input.txt") as file:
    sum = 0

    first, second = [line.rstrip() for line in file]
    times_tostrip = first.split(' ')[1:]
    distances_tostrip = second.split(' ')[1:]

    times = []
    for time in times_tostrip:
        if time != '':
            times.append(time)

    distances = []
    for distance in distances_tostrip:
        if distance != '':
            distances.append(distance)

    time_str = ""
    distance_str = ""

    for t in times:
        time_str += t

    time = int(time_str)

    for d in distances:
        distance_str += d
    distance = int(distance_str)

    print(time)
    print(distance)

    for t in range(time):
        race_dist = t * (time - t)
        if race_dist > distance:
            sum += 1

    print(sum)


