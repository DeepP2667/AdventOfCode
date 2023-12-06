with open("input.txt", 'r') as file:
    lines = file.readlines()

# PART 1
total = 0
for game in lines:
    cards = game.split(":")[1]
    winning = cards.split("|")[0].strip().split(" ")
    your_cards = cards.split("|")[1].strip().split(" ")
    
    winning_set = set(winning)
    if '' in winning_set:
        winning_set.remove('')
    your_cards_set = set(your_cards)
    if '' in your_cards_set:
        your_cards_set.remove('')

    set_score = 0
    first = True
    for card in your_cards_set:
        if card in winning_set:
            if first:
                set_score = 1
                first = False
            else:
                set_score *= 2


    total += set_score

print(total)


# PART 2
from collections import defaultdict

cards_counter = defaultdict(int)
for card_num, c in enumerate(lines):
    cards = c.split(":")[1]
    winning = cards.split("|")[0].strip().split(" ")
    your_cards = cards.split("|")[1].strip().split(" ")
    
    winning_set = set(winning)
    if '' in winning_set:
        winning_set.remove('')
    your_cards_set = set(your_cards)
    if '' in your_cards_set:
        your_cards_set.remove('')

    card_num = card_num + 1
    cards_counter[card_num] += 1
    next_card = card_num + 1
    for card in your_cards_set:
        if card in winning_set:
            cards_counter[next_card] += cards_counter[card_num]
            next_card += 1

print(sum(cards_counter.values()))