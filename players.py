class Player:
    def __init__(self, name):
        self.name = name

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

