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
      return int(self.num)
    else:
      return 10



class Player:
  def __init__(self, card1, card2, name):
    self.name = name
    self.hands = [0,0]
    if card1 == card2:
      self.hands[0] += int(card1.val())
      self.hands[1] += int(card2.val())
    else:
      self.hands[0] += int(card1.val()) + int(card2.val())
  def __str__(self):
    return self.name+" "+str(self.hands)
  def play(self, deck):
    for x in range(len(self.hands) - 1):
      if (self.hands[x] <= 16):
        self.hands[x] += int(deck.draw().val())
        print("Hit")
      print("Stand")


class Dealer:
  def __init__(self, ps):
    self.players = []
    self.numplay = ps
    self.deck = Deck()
    self.deck.create_deck()
    print(self.deck)
    for i in range(self.numplay):
      card1 = self.deck.draw()
      card2 = self.deck.draw()
      self.players.append(Player(card1, card2, str(i)))

  def turn(self):
    for i in range(len(self.players)-1):
      self.players[i].play(self.deck)
      print(self.players[i])

d = Dealer(2)
d.turn()

# d = Deck()
# d.create_deck()
# print(d)
# print(d.draw())

# p1 = Player(d.draw(), d.draw(), "Test1")
# dealer = Dealer(d.draw(), d.draw())

# p1.play(d)
# dealer.play(d)
