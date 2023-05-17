import random


class Player:
    def __init__(self, name):
        self.name = name
        # Give each player an initial chip count of 1000
        self.chips = 1000

    def chooser(self, card):
        if card[0] == card[1]:
            return card[0]
        else:
            return card[0]

    def init(self, card1, card2):
        # self.hands = [0, 0]
        self.stand = False
        if card1 == card2:
            self.hands = [
                int(self.chooser(card1.val())),
                int(self.chooser(card2.val())),
            ]
        else:
            self.hands = [
                int(self.chooser(card1.val())) + int(self.chooser(card2.val()))
            ]

    def play(self, deck, dealer):
        # print("the dealers card is: " + dealer.up.__str__())
        for x in range(len(self.hands)):
            while self.hands[x] <= 16:
                print(self.name + " Hit " + str(self.hands[x]))
                self.hands[x] += int(self.chooser(deck.draw().val()))
            if self.hands[x] > 21:
                print(self.name + " Bust " + str(self.hands[x]))
            else:
                print(self.name + " Stand " + str(self.hands[x]))
                self.stand = True

    def bet(self, amount):
        # Deduct bet amount from player's chips and store current bet amount
        if amount > 0 and amount <=self.chips:
            print(f"{self.name} bets {amount}")
            self.current_bet = amount
            self.chips -= amount


class RandomPlayer(Player):

  def play(self, deck, dealer):
    for x in range(len(self.hands)):
      while self.hands[x] <= 16:
        if random.choice([True, False]):
          print(self.name + " Hit " + str(self.hands[x]))
          self.hands[x] += int(self.chooser(deck.draw().val()))
        else:
          break
      if self.hands[x] > 21:
        print(self.name + " Bust " + str(self.hands[x]))
      else:
        print(self.name + " Stand " + str(self.hands[x]))
        self.stand = True


class BasicStrategyPlayer(Player):

  def play(self, deck, dealer):
    dealer_upcard = int(self.chooser(dealer.up.val()))
    for x in range(len(self.hands)):
      while self.hands[x] <= 16:
        if dealer_upcard in [2, 3]:
          if self.hands[x] >= 13:
            break
        elif dealer_upcard in [4, 5, 6]:
          if self.hands[x] >= 12:
            break
        elif dealer_upcard == 7 or dealer_upcard == 8:
          if self.hands[x] >= 17:
            break
        else:
          if self.hands[x] >= 18:
            break
        print(self.name + " Hit " + str(self.hands[x]))
        self.hands[x] += int(self.chooser(deck.draw().val()))
      if self.hands[x] > 21:
        print(self.name + " Bust " + str(self.hands[x]))
      else:
        print(self.name + " Stand " + str(self.hands[x]))
        self.stand = True


class CardCounter(Player):

  def __init__(self, name):
    super().__init__(name)
    self.count = 0

  def play(self, deck, dealer):
    for x in range(len(self.hands)):
      while self.hands[x] <= 16:
        if self.count >= 2:
          print(self.name + " Hit " + str(self.hands[x]))
          card = deck.draw()
          self.update_count(card)
          self.hands[x] += int(self.chooser(card.val()))
        else:
          break
      if self.hands[x] > 21:
        print(self.name + " Bust " + str(self.hands[x]))
      else:
        print(self.name + " Stand " + str(self.hands[x]))
        self.stand = True

  def update_count(self, card):
    if card.num in ['2', '3', '4', '5', '6']:
      self.count += 1
    elif card.num in ['10', 'Jack', 'Queen', 'King', 'Ace']:
      self.count -= 1