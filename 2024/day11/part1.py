def blink(stones):
    new_stones = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            new_stones.extend([int(stone_str[:int(len(stone_str)/2)]), int(stone_str[int(len(stone_str)/2):])])
        else:
            new_stones.append(stone * 2024)
        
    return new_stones

with open("input.txt") as file:
    stones = [int(i) for i in file.readline().split()]

    for _ in range(25):
        stones = blink(stones)
    
    print(len(stones))

    