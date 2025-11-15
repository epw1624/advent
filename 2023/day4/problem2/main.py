

def main():
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]

        num_cards = [1 for _ in range(len(lines))]

        for i in range(len(lines)):
            nums = lines[i].split(':')[1]
            win_str, your_str = nums.split('|')
            winners = [int(i) for i in win_str.split(' ') if i.strip()]
            yours = [int(i) for i in your_str.split(' ') if i.strip()]
            matches = get_matches(winners, yours)

            for j in range(matches):
                num_cards[i+j+1] += num_cards[i]


        total_cards = 0
        for num in num_cards:
            total_cards += num

    print(total_cards)
            
def get_matches(winners, yours):
    matches = 0
    for num in yours:
        if num in winners:
            matches += 1

    return matches


main()