from functools import cmp_to_key

CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

FIVE = 6
FOUR = 5
FULL = 4
THREE = 3
TWO = 2
ONE = 1

class Hand:
    def __init__(self, score, hand):
        self.cards = hand
        self.score = score
        self.bid = 0

    def comparator(hand1, hand2):
        if type(hand2) == Hand:
            if hand1.score > hand2.score:
                return 1
            elif hand2.score > hand1.score:
                return -1
            else:
                for i in range(5):
                    card1 = CARDS.index(hand1.cards[i])
                    card2 = CARDS.index(hand2.cards[i])
                    if card1 > card2:
                        return -1
                    elif card2 > card1:
                        return 1
                return 0

def main():
    total = 0
    with open("input.txt") as file:
        hands = []
        lines = [line.rstrip() for line in file]
        for line in lines:
            hand, bid = line.split(' ')
            hand_obj = get_score(hand)
            hand_obj.bid = int(bid)
            hands.append(hand_obj)

        hands = sorted(hands, key=cmp_to_key(Hand.comparator))

        for i in range(len(hands)):
            total += (i + 1) * (hands[i].bid)

    print(total)


# wrapper for get_score that handles the 3-tuple format
def sort_hands(hand):
    return get_score(hand[1])

def sorting_order(char):
    return CARDS.index(char)

def get_score(hand):
    score = 0

    cards = []
    for char in hand:
        cards.append(char)

    cards_sorted = sorted(cards, key=sorting_order)

    card_types = []
    cur_char = cards_sorted[0]
    count = 0
    for char in cards_sorted:
        if char != cur_char:
            card_types.append(count)
            count = 1
            cur_char = char
        else:
            count += 1
    card_types.append(count)
    card_types = sorted(card_types)
    card_types.reverse()

    # get score for hand type
    match card_types[0]:
        case 5:
            score += FIVE
        case 4:
            score += FOUR
        case 3:
            if len(card_types) == 2:
                score += FULL
            else:
                score += THREE
        case 2:
            if card_types[1] == 2:
                score += TWO
            else:
                score += ONE

    return Hand(score, cards)



main()



