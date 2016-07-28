# Project Euler 54

card_value_dict = {
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        'T' : 10,
        'J' : 11,
        'Q' : 12,
        'K' : 13,
        'A' : 14
    }

# rank in tuples:  (type of hand, high card, next card)

def card_value(card):
    "Returns the numeric card value."
    return card_value_dict[card]

def is_straight(hand):
    """Detects whether the hand (a list of cards) is a straight."""
    card_numbers = {card_value(card[0]) for card in hand}
    lowest_card = min(card_numbers)
    if card_numbers == set(range(lowest_card,lowest_card+5)):
        return True
    else:
        return False

def is_flush(hand):
    """Detects whether the hand (a list of cards) is a flush."""
    suits = {card[1] for card in hand}
    if len(suits) == 1:
        return True
    else:
        return False

def is_quad(hand):
    card_numbers = [card_value(card[0]) for card in hand]
    for n in card_numbers:
        if card_numbers.count(n) == 4:
            return True
        else:
            return False

def is_trip(hand):
    card_numbers = [card_value(card[0]) for card in hand]
    for n in card_numbers:
        if card_numbers.count(n) == 3:
            return True
        else:
            return False

def is_pair(hand):
    card_numbers = [card_value(card[0]) for card in hand]
    number_of_pairs = 0
    for n in card_numbers:
        if card_numbers.count(n) == 2:
            number_of_pairs += 1
    if number_of_pairs == 1:
        return True
    else:
        return False

def is_two_pair(hand):
    card_numbers = [card_value(card[0]) for card in hand]
    number_of_pairs = 0
    for n in card_numbers:
        if card_numbers.count(n) == 2:
            number_of_pairs += 1
    if number_of_pairs == 2:
        return True
    else:
        return False

def hand_rank(hand):
    card_numbers = sorted([card_value(card[0]) for card in hand])[::-1]
    if is_straight(hand) and is_flush(hand):
        return (8, card_numbers)
    if is_quad(hand):
        return (7, card_numbers)
    if is_trip(hand) and is_pair(hand):
        return (6, card_numbers)
    if is_flush(hand):
        return (5, card_numbers)
    if is_straight(hand):
        return (4, card_numbers)
    if is_trip(hand):
        return (3, card_numbers)
    if is_two_pair(hand):
        return (2, card_numbers)
    if is_pair(hand):
        return (1, card_numbers)
    else:
        return (0, card_numbers)

def judge_hands(hand1,hand2):
    rank1 = hand_rank(hand1)
    rank2 = hand_rank(hand2)
    if rank1[0] > rank2[0]:
        return 1
    elif rank2[0] > rank1[0]:
        return 2
    else:
        for j in range(5):
            if rank1[1][j] > rank2[1][j]:
                return 1
            elif rank2[1][j] > rank1[1][j]:
                return 2

player_one_count = 0

with open("54-poker.txt","r") as input_file:
    raw_hands_list = input_file.readlines()
    for j in range(len(raw_hands_list)):
        hand1 = [raw_hands_list[j][3*k:3*k+2] for k in range(5)]
        hand2 = [raw_hands_list[j][3*k:3*k+2] for k in range(5,10)]
        if judge_hands(hand1,hand2) == 1:
            player_one_count += 1

print(player_one_count) # 376

