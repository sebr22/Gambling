import random


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
      return [int(self.num),int(self.num)]
    elif self.num == "Ace":
      return [1,11]
    else:
      return [10,10]


class Player:

  def __init__(self, name):
    self.name = name

  def chooser(self, card):
    if (card[0]==card[1]):
      return card[0]
    else:
      return card[0]
    
  def init(self, card1, card2):
    self.hands = [0, 0]
    if card1 == card2:
      self.hands[0] += int(self.chooser(card1.val()))
      self.hands[1] += int(self.chooser(card2.val()))
    else:
      self.hands[0] += int(self.chooser(card1.val())) + int(self.chooser(card2.val()))

  def __str__(self):
    return self.name + " " + str(self.hands)

  def play(self, deck):
    for x in range(len(self.hands) - 1):
      if (self.hands[x] <= 16):
        self.hands[x] += int(self.chooser(deck.draw().val())) 
        print("Hit")
      else:
        print("Stand")


class Game:

  def __init__(self, p):
    # DOESN'T INCLUDE "DEALER" WHICH IS AUTO GENERATED
    self.players = p
    self.deck = Deck()
    self.deck.create_deck()
    print(self.deck)
    for i in range(len(self.players)):
      card1 = self.deck.draw()
      card2 = self.deck.draw()
      self.players[i].init(card1, card2)
    self.players.insert(0, Player("DEALER"))
    dcard1 = self.deck.draw()
    dcard2 = self.deck.draw()
    self.players[0].init(dcard1, dcard2)

  def turn(self):
    for i in range(len(self.players)):
      self.players[i].play(self.deck)
      print(self.players[i])
      print("\n")


d = Game([Player("p1"), Player("p2")])
d.turn()
