import time
import logging

logging.basicConfig(
    filename='output.log',
    level=logging.INFO,
    format='%(message)s'
)

X = 101
Y = 103

def pretty_print_map(map, t):
    logging.info(f"Time = {t}")
    for line in map:
        logging.info(''.join(line))

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    # (x, y, dx, dy)
    robots = [(int(robot.split(',')[0].split('=')[-1]), int(robot.split(',')[1].split(' ')[0]), int(robot.split('=')[2].split(',')[0]), int(robot.split(',')[-1])) for robot in lines]

    t = 0
    while True:
        t += 1
        map = [['.' for x in range(X)] for y in range(Y)]
        for i, robot in enumerate(robots): # lol
            x, y, dx, dy = robot
            robots[i] = ((x+dx)%X, (y+dy)%Y, dx, dy)
            map[(y+dy)%Y][(x+dx)%X] = '^'

        
        if t % 101 == 18:
            pretty_print_map(map, t)
