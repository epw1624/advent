X = 101
Y = 103
T = 100

Q1 = ((0, X // 2 - 1), (0, Y // 2 - 1))
Q2 = ((X // 2 + 1, X - 1), (0, Y // 2 - 1))
Q3 = ((0, X // 2 - 1), (Y // 2 + 1, Y - 1))
Q4 = ((X // 2 + 1, X - 1), (Y // 2 + 1, Y - 1))

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    q1, q2, q3, q4 = 0, 0, 0, 0

    for robot in lines:
        x = int(robot.split(',')[0].split('=')[-1])
        y = int(robot.split(',')[1].split(' ')[0])

        dx = int(robot.split('=')[2].split(',')[0])
        dy = int(robot.split(',')[-1])

        x_final = (x + T * dx) % X
        y_final = (y + T * dy) % Y

        if x_final >= Q1[0][0] and x_final <= Q1[0][1] and y_final >= Q1[1][0] and y_final <= Q1[1][1]:
            q1 += 1
        elif x_final >= Q2[0][0] and x_final <= Q2[0][1] and y_final >= Q2[1][0] and y_final <= Q2[1][1]:
            q2 += 1
        elif x_final >= Q3[0][0] and x_final <= Q3[0][1] and y_final >= Q3[1][0] and y_final <= Q3[1][1]:
            q3 += 1
        elif x_final >= Q4[0][0] and x_final <= Q4[0][1] and y_final >= Q4[1][0] and y_final <= Q4[1][1]:
            q4 += 1

    print(q1*q2*q3*q4)