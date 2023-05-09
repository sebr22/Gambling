class deck:
  cardList = []
  def draw():
    card = cardList[0]
    cardList.pop(0)
    return card
    
class card:
  def __init__(s, number, c):
    self.suit = suit
    self.num = number
    self.count = c

	
class player:
  listOfCards = []
  count = 0
  cardCount = 0

