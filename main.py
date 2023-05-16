import random
# add another import for other player classes
from players import Player
from players import BasicStrategyPlayer
from players import CardCounter
from players import RandomPlayer

class Deck:
    def __init__(self):
        self.cardList = []
        self.drawnCards = []

    def create_deck(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        numbers = [str(x) for x in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
        for suit in suits:
            for number in numbers:
                self.cardList.append(Card(suit, number))
        random.shuffle(self.cardList)
        return self.cardList

    def __str__(self):
        ret = ""
        for x in self.cardList:
            ret += x.__str__() + "\n"
        return ret

    def draw(self):
        card = self.cardList[0]
        self.cardList.pop(0)
        self.drawnCards.append(card)
        return card


class Card:
    def __init__(self, s, number):
        self.suit = s
        self.num = number

    def __str__(self):
        return str(self.num) + " of " + self.suit

    def __eq__(self, other):
        return self.num == other.num

    def val(self):
        if self.num.isdigit():
            return [int(self.num), int(self.num)]
        elif self.num == "Ace":
            return [1, 11]
        else:
            return [10, 10]


class Dealer:
    def aces(self, card):
        if card[0] == card[1]:
            return card[0]
        else:
            return card[0]

    def __init__(self, deck):
        self.deck = deck
        self.up = self.deck.draw()
        self.count = self.aces(self.up.val())

    def play(self):
        while self.count <= 16:
            self.count += int(self.aces(self.deck.draw().val()))
            print("Dealer Hit")
        if self.count > 21:
            print("Dealer Bust")
        else:
            print("Dealer Stand")
            self.stand = True


deck = Deck()
deck.create_deck()

players = [Player("Player"), BasicStrategyPlayer("Basic"), CardCounter("Card Counter"), RandomPlayer("Rando")]
dealer = Dealer(deck)
for p in range(len(players)):
    players[p].init(deck.draw(), deck.draw())

for p in range(len(players)):
    players[p].play(deck, dealer)
    print("\n")
dealer.play()

for p in players:
    if p.hands[0] > dealer.count and p.hands[0] <= 21:
        print(p.name + " beats the dealer")
