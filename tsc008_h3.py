import random


class Wish:
    CARD_COLORS = ['\u2660', '\u2666', '\u2663', '\u2665']
    CARD_RANGE = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.tableaus = {
            'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [],
            'g': [], 'h': []}
        self.init_game()

    def init_deck(self):
        'fills a deck with correct amount of cards'
        deck = []
        for suit in Wish.CARD_COLORS:
            for number in Wish.CARD_RANGE:
                card = f'{suit}{number}'
                deck.append(card)
        return deck

    def init_game(self):
        'sets up tableaus'
        deck = self.init_deck()
        while len(deck) > 0:
            for tableau in self.tableaus:
                card_num = random.randint(0, len(deck) - 1)
                card = deck.pop(card_num)
                self.tableaus[tableau].append(card)

    def game_loop(self):
        while True:
            self.display_round()
            self.check_options()
            cards = self.choose_cards()
            self.remove_cards(cards)


    def check_options(self):


    def display_round(self):
        'displays game state'
        letter_row = ''
        top_row = ''
        tableau_num = ''
        for tableau in sorted(self.tableaus):
            stack = self.tableaus[tableau]
            letter_row += f'{tableau}'.rjust(4)
            top_row += f'{stack[0]}'.rjust(4)
            tableau_num += f'{len(stack)}'.rjust(4)

        print(letter_row)
        print(top_row)
        print(tableau_num)

    def choose_cards(self):
        while True:
            choose_cards = input('Velg to bunker: ').lower()
            if len(choose_cards) != 2:
                print('Ikke korrekt lengde på input')
                continue
            if len(self.tableaus.get(choose_cards[0], [])) < 1:
                print(f'"{choose_cards[0]}" er ikke et gyldig valg')
                continue
            if len(self.tableaus.get(choose_cards[1], [])) < 1:
                print(f'"{choose_cards[1]}" er ikke et gyldig valg')
                continue
            break
        return choose_cards


new_game = Wish()
new_game.game_loop()
