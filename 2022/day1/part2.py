with open("input.txt") as file:
    calories = []
    current_calories = 0
    for line in file:
        if line.rstrip() != '':
            current_calories += int(line.rstrip())
        else:
            calories.append(current_calories)
            current_calories = 0
    
    calories.sort()
    print(calories[-1] + calories[-2] + calories[-3])

