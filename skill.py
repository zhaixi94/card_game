
get_card_level = lambda x: x.level


def test_skill(deck):
    card_levels = list(map(get_card_level,deck))
    chosen_card = None
    for i in range(-1,-len(card_levels)-1,-1):
        card_level = card_levels[i]
        if card_level == 7:
            chosen_card = deck[i]
            del deck[i]
            break

    print(f"因技能选择{chosen_card.card_name}放至卡组最顶端")
    deck.append(chosen_card)
    return deck

