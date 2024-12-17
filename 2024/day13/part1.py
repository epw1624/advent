import numpy as np

tolerance = 1e-9

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    machines = [lines[i:i+3] for i in range(0, len(lines), 4)]

    tokens = 0

    for machine in machines:
        xa = int(machine[0].split(',')[0].split('+')[-1])
        ya = int(machine[0].split(',')[1].split('+')[-1])

        xb = int(machine[1].split(',')[0].split('+')[-1])
        yb = int(machine[1].split(',')[1].split('+')[-1])

        prize_x = int(machine[2].split(',')[0].split('=')[-1])
        prize_y = int(machine[2].split(',')[-1].split('=')[-1])

        m = np.array([[xa, xb], [ya, yb]])
        b = np.array([prize_x, prize_y])

        try:
            x = np.linalg.solve(m, b)

            a, b = x

            if abs(a - round(a)) < tolerance and abs(b - round(b)) < tolerance:
                tokens += 3 * round(a) + round(b)

        except np.linalg.LinAlgError:
            pass

    print(tokens)