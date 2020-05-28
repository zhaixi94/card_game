from decks import *
from skill import *

def card_effect(effect_card, can_use_card, deck, hands,effect_cards,need_card=None):
    print(f"发动 {effect_card.card_name}")
    choose,deck = effect_card.effect(deck, effect_cards)

    # 优先拿需要的卡
    chosen = False
    if need_card:
        print(f"需要{need_card}")
        for need_ca in need_card:
            for j in range(len(choose)):
                card = choose[j]
                if card.card_name == need_ca:
                    print(f"挑选{card.card_name}加入手牌")
                    chosen = True
                    deck = effect_card.chosen(choose, j, deck, hands)
                    break
            if chosen:
                break
        # for j in range(len(choose)):
        #     card = choose[j]
        #     if card.card_name in need_card:
        #         print(f"挑选{card.card_name}加入手牌")
        #         chosen = True
        #         deck = effect_card.chosen(choose, j, deck, hands)
        #         break
        if not chosen:
            deck = deck+choose

    else:  # 检索拿手上没有的牌，如果都有就不拿
        for j in range(len(choose)):
            card = choose[j]
            # print(f"can_used_card : {can_use_card}")
            if card.card_name not in can_use_card:
                print(f"挑选{card.card_name}加入手牌")
                chosen = True
                deck = effect_card.chosen(choose, j, deck, hands)
                break
        if not chosen:
            deck = deck + choose
    return hands,deck


if __name__ == "__main__":
    results = []
    import copy
    for i in range(1000):
        hands = [] # 手牌
        monster = []  #怪兽区
        magic_trap = [] # 魔陷区
        effect_cards = []  # 已经发动的卡名称

        deck = copy.deepcopy(decks1)
        random.shuffle(deck)

        # 技能发动
        deck = test_skill(deck)

        # 抽卡
        card_nums = 4
        print(f"抽卡，数量为{card_nums}")
        for i in range(card_nums):
            card_obj = deck.pop()
            hands.append(card_obj)

        f = lambda x: x.card_name
        hands_name = list(map(f, hands))
        print(f"手牌 {hands_name}")


        hands = sorted(hands,key=lambda x:len(x.card_name)) # 为使得魔导阵在仗前面被循环到

        # 有魔导阵先发动魔导阵
        i = -1
        while True:
            i = i+1
            if i == len(hands):
                break

            card = hands[i]

            if card.card_name == "黑魔导阵" and card.card_name not in effect_cards:
                effect_card = hands[i]
                del hands[i]
                i = i-1
                magic_trap.append(effect_card)
                can_use_card = list(map(f,hands+magic_trap+monster))
                if "黑魔导" not in can_use_card and (not {"黑魔导权杖","幻象魔术"}.issubset(set(can_use_card))):
                    hands, deck = card_effect(effect_card, can_use_card, deck, hands, effect_cards,['黑魔导',"幻象魔术"])
                else:
                    hands, deck = card_effect(effect_card,can_use_card,deck,hands,effect_cards)
                continue

            if card.card_name == "黑魔导权杖" and card.card_name not in effect_cards:
                effect_card = hands[i]
                del hands[i]
                i = i-1
                monster.append(effect_card)
                can_use_card = list(map(f,hands+magic_trap+monster))
                if "黑魔导阵" not in can_use_card:
                    hands, deck = card_effect(effect_card, can_use_card, deck, hands, effect_cards,["黑魔导阵"])
                elif "魔术师导航" not in can_use_card:
                    hands, deck = card_effect(effect_card, can_use_card, deck, hands, effect_cards, ["魔术师导航"])
                else:
                    hands, deck = card_effect(effect_card, can_use_card, deck, hands,effect_cards)

        hands_name = list(map(f,hands))
        print(f"手牌{hands_name}")
        print(f"魔陷区{list(map(f,magic_trap))}")
        print(f"怪兽区{list(map(f,monster))}")
        print(f"卡组数量 {len(deck)}")

        can_use_card = list(map(f, hands + magic_trap + monster))
        if {"黑魔导","魔术师导航","黑魔导阵"}.issubset(set(can_use_card)) or \
            {"黑魔导权杖","幻象魔术","魔术师导航","黑魔导阵"}.issubset(set(can_use_card)):
            result = "胡牌"
        elif{"黑魔导","魔术师导航"}.issubset(set(can_use_card)) or \
            {"黑魔导权杖","幻象魔术","魔术师导航"}.issubset(set(can_use_card)):
            result = "可展开"
        else:
            result = "卡手"
        results.append(result)
    print("胡牌次数 : ",results.count("胡牌"))
    print("可展开次数 : ",results.count("可展开"))


