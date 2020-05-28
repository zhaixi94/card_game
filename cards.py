import random

get_card_name = lambda x: x.card_name

class basecard:
    def __init__(self):
        self.card_name = ""
        self.type = 0 # 0 monster 1,magic 2,trap
        self.key_word = ""
        self.level = 0


class black_magician(basecard):
    def __init__(self):
        super(black_magician,self).__init__()
        self.card_name = "黑魔导"
        self.key_word = "黑魔导"
        self.level = 7


class dark_magicial_circle(basecard):
    def __init__(self):
        super(dark_magicial_circle, self).__init__()
        self.card_name = "黑魔导阵"
        self.key_word = "黑魔导"
        self.type = 1

    def effect(self,deck,effected_cards):
        if "黑魔导阵" in effected_cards:
            return [],deck

        effect_cards = []
        for i in range(3):
            effect_cards.append(deck.pop())

        print(f"牌组上方三张牌是{list(map(get_card_name,effect_cards))}")
        get_keywrds =  lambda x: x.key_word
        effect_cards_key_words = list(map(get_keywrds,effect_cards))

        choose = []
        unchoose = []
        for i in range(len(effect_cards)):
            key_word = effect_cards_key_words[i]
            if key_word == "黑魔导":
                choose.append(effect_cards[i])
            else:
                unchoose.append(effect_cards[i])
        deck = deck + unchoose
        print(f"可加入手牌的卡有{list(map(get_card_name,choose))}")
        effected_cards.append("黑魔导阵")
        return choose,deck

    def chosen(self,choose,chosen,decks,hands):
        chosen_cards = choose[chosen]
        hands.append(chosen_cards)
        del choose[chosen]
        decks = decks + choose
        print("洗牌")
        random.shuffle(decks)
        return decks


class magician_navigation(basecard):
    def __init__(self):
        super(magician_navigation, self).__init__()
        self.card_name = "魔术师导航"
        self.key_word = "黑魔导"
        self.type = 2


class magicians_rod(basecard):
    def __init__(self):
        super(magicians_rod, self).__init__()
        self.card_name = "黑魔导权杖"
        self.level = 3

    def effect(self,deck,effected_cards):
        if "黑魔导权杖" in effected_cards:
            return [],deck

        choose = []
        unchoose = []
        for i in range(len(deck)):
            card = deck.pop()
            if card.key_word == "黑魔导" and card.type != 0:
                choose.append(card)
            else:
                unchoose.append(card)
        deck = unchoose
        print(f"可选择卡牌{list(map(get_card_name,choose))}")
        effected_cards.append("黑魔导权杖")
        return choose,deck

    def chosen(self,choose,chosen,decks,hands):
        chosen_cards = choose[chosen]
        hands.append(chosen_cards)
        del choose[chosen]
        decks = decks + choose
        print("洗牌")
        random.shuffle(decks)
        return decks



class illution_magic(basecard):
    def __init__(self):
        super(illution_magic, self).__init__()
        self.card_name = "幻象魔术"
        self.key_word = "黑魔导"
        self.type = 1


class maigician_of_dark_illusion(basecard):
    def __init__(self):
        super(maigician_of_dark_illusion, self).__init__()
        self.card_name = "黑魔术幻象"
        self.level = 7


