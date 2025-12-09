with open("input.txt") as file:
    calories = 0
    max_calories = 0
    for line in file:
        if line.rstrip() != '':
            calories += int(line.rstrip())
        else:
            max_calories = max(max_calories, calories)
            calories = 0
    
    print(max_calories)

