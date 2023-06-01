import random
from players import Player
from players import BasicStrategyPlayer
from players import CardCounter
from players import RandomPlayer
from players import MITCardCounter
import csv
import glob
#set verbose to either 1 or 0. 1 = verbose 0 = not verbose.
verbose = 0
file = "output/"+str(len(glob.glob('./output/*')))+".csv"
fp = open(file, 'x')
fp.close()

with open(file, mode='a') as list:
    data = csv.writer(list)
    data.writerow(["Dealer_Up", "Drawn_Cards", "Num_of_Hits", "Seat_At_Table", "Did_YOU_Win"])



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

  def arr(self):
    ret = []
    for i in self.drawnCards:
      ret.append(i.__str__())
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
    self.drawn = []
    self.hits = 0
		# if verbose == 1:
		# 	print("Drawn :", self.drawn, "")

  def play(self):
    self.down = self.deck.draw()
    while self.count <= 16:
      new_card = self.deck.draw()
      self.count += int(self.aces(new_card.val()))
      self.drawn.append(new_card.__str__())
      self.hits += 1
      print("Dealer Hit")
    if self.count > 21:
      print("Dealer Bust")
    else:
      print("Dealer Stand")
      self.stand = True


class Tournament:

  def __init__(self, players, rounds):
    self.players = players
    self.rounds = rounds
    self.win_rates = {player.name: 0 for player in players}

  def play_round(self):
    deck = Deck()
    deck.create_deck()
    dealer = Dealer(deck)

    # Update count for all players when dealer's up card is revealed
    # for p in range(len(self.players)):
    #     if isinstance(self.players[p], CardCounter):
    #       self.players[p].update_count(dealer.up)

    for p in range(len(self.players)):
      card1 = deck.draw()
      card2 = deck.draw()

      # Update count for all players when player's initial cards are dealt
      # if isinstance(self.players[p], CardCounter):
      #   self.players[p].update_count(card1)
      #   self.players[p].update_count(card2)

      # Allow player to make a bet
      bet = min(100, self.players[p].chips)
      self.players[p].bet(bet)

      # Initialize player's hand
      self.players[p].init(card1, card2)
			
    for p in range(len(self.players)):
      # Allow player to play their hand
      self.players[p].play(deck, dealer)
      print("\n")

    # Allow dealer to play their hand
    dealer.play()
    print("\n")

    # Determine outcome of round for each player
    for p in range(len(self.players)):
      self.win = False
      if ((self.players[p].hands[0] > dealer.count) or
          (dealer.count > 21)) and (self.players[p].hands[0] <= 21):
        print(self.players[p].name + " beat the dealer with a count of " +
              str(self.players[p].hands[0]))
        self.win = True
        # Player wins and receives double their bet
        winnings = 2 * self.players[p].current_bet
        self.players[p].chips += winnings

        # Update win rate for player
        self.win_rates[self.players[p].name] += 1 / self.rounds
      else:
        print(self.players[p].name + " lost to the dealer with a count of " +
              str(self.players[p].hands[0]))
        # Player loses and loses their bet
        loss = -1 * self.players[p].current_bet
        self.players[p].chips += loss
      with open(file, mode='a') as list:
        data = csv.writer(list)
        data.writerow([dealer.up, self.players[p].drawnatm, self.players[p].hits, p, (1 if self.win else 0)])


  def play_tournament(self):
    for round_num in range(1, self.rounds + 1):
      print(f"Round {round_num}")
      print("--------")

      # Play a round of the tournament
      self.play_round()

    # Determine winner of tournament
    max_chips = max([p.chips for p in self.players])
    winner = next(p for p in self.players if p.chips == max_chips)
    print(f"{winner.name} has won the tournament with {winner.chips} chips")

  def display_win_rates(self):
    print("\nWin Rates:")
    for player_name, win_rate in self.win_rates.items():
      print(f"{player_name}: {win_rate:.2f}")


players = [
  Player("Player"),
  BasicStrategyPlayer("Basic"),
  CardCounter("Card Counter"),
  RandomPlayer("Rando"),
  MITCardCounter("MIT")
]
tournament = Tournament(players, 100)
tournament.play_tournament()
tournament.display_win_rates()