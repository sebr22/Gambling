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
    return self.num==other.num


class Player:
  def __init__(self, card1, card2, name):
    self.name = name
    self.hands = []
    if (card1==card2):
      self.hands[0]+=card1.num
      self.hands[1]+=card2.num
    else:
      self.hands[0]+=(card1.num+card2.num)
    
  def play(self, hand, deck):
    for x in range(0,self.hands.len-1):
      if (self.hands[x]<=16):
        self.hands[x]+=deck.draw()
        print("Hit")
      print("Stand")

 class Dealer(self, hand, deck, Player): 
   def __init__(self, card1, card2):
     super(self, card1, card2, "Dealer")
   
     
      
d = Deck()
d.create_deck()
print(d)
print(d.draw())

p1 = Player(d.draw(), d.draw(), "Test1")
dealer = Dealer(d.draw(), d.draw())

p1.play(d)
dealer.play(d)


  