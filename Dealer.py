import random
from enum import Enum
from Player import Player

class Suit(Enum):
    HEARTS = 0
    DIAMONDS = 1
    CLUBS = 2
    SPADES = 3

class Dealer:

    def __init__(self):
        self.deck = {Suit.HEARTS: [], Suit.DIAMONDS: [], Suit.CLUBS: [], Suit.SPADES: []}
        self.hand = []
        self.total = 0

        for i in range(4):
            for j in range(1, 14):
                self.deck[Suit(i)].append(j)

    def deal(self, player: Player) -> None:
        for i in range(2):
            self.hand.append(self.get_rand_card())
        for i in range(2):
            player.hand.append(self.get_rand_card())
        self.total = Dealer.score_calculator(self.hand)
        player.total = Dealer.score_calculator(player.hand)

    def deal_hit(self, player: Player) -> None:
        card = self.get_rand_card()
        #Add the cards value to the players total

        player.hand.append(card)
        player.total = Dealer.score_calculator(player.hand)

    def get_rand_card(self) -> tuple:
        while True:
            rand_suit, nums = random.choice(list(self.deck.items()))
            if nums:
                rand_num = random.choice(nums)
                break
        self.deck[rand_suit].remove(rand_num)
        return rand_suit, rand_num

    @staticmethod
    def score_calculator(hand) -> int:
        total = 0

        for i in range(len(hand)):
            if hand[i][1] >= 10:
                total += 10
            else:
                total += hand[i][1]
        return total

    def deal_own(self) -> None:
        #Add cards until 17 or greater.
        while self.total < 17:
            card = self.get_rand_card()
            self.hand.append(card)
            self.total = Dealer.score_calculator(self.hand)


    def check_win(self, player: Player) -> bool:
        dealer_score = self.total
        player_score = player.total

        if player_score > 21:
            return False
        elif dealer_score > 21:
            return True
        elif player_score == dealer_score:
            return False
        elif player_score < dealer_score:
            return False
        elif player_score > dealer_score:
            return True
        return True