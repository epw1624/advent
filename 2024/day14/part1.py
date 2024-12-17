with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    safety_factor = 1

    for robot in lines:
        x = int(robot.split(',')[0].split('=')[-1])
        y = int(robot.split(',')[1].split(' ')[0])

        dx = int(robot.split('=')[2].split(',')[0])
        dy = int(robot.split(',')[-1])

        print(f"x={x}, y={y}, dx={dx}, dy={dy}")