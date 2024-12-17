from util.decorators import timer
from functools import cache

@cache
def count_stones(stone, blinks):
    if blinks == 0:
        return 1
    
    if stone == 0:
        return count_stones(1, blinks - 1)
    else:
        stone_str = str(stone)
        if len(stone_str) % 2 == 0:
            left = int(stone_str[:len(stone_str)//2])
            right = int(stone_str[len(stone_str)//2:])
            return count_stones(left, blinks - 1) + count_stones(right, blinks - 1)
        else:
            return count_stones(stone * 2024, blinks - 1)

@timer
def part2():
    with open("day11/input.txt") as file:
        stones = [int(i) for i in file.readline().split()]

        num_stones = sum(count_stones(stone, 75) for stone in stones)
        print(num_stones)

if __name__ == "__main__":
    part2()
