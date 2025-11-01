from Player import Player
from Dealer import Dealer
from Dealer import Suit

class Game:
    def __init__(self, name: str, balance: int):
        self.player = Player(name, balance)
        self.dealer = Dealer()

    def play(self):
        print(f"Hello {self.player.name}! Welcome to Black Jack!! 💰💰💰")
        print("------------------------------------\n")

        while True:
            self.dealer = Dealer()
            self.player.hand = []
            self.player.total = 0

            if self.player.balance == 0:
                print("Dang your broke...")
                break

            ans = ""
            bet = 0
            while True:
                ans = input("How much will you bet?\n")
                bet = int(ans)
                if self.player.balance < bet:
                    print(f"You do not have sufficient funds. Current balance: {self.player.balance}")
                else:
                    self.player.balance -= bet
                    print(f"-${bet}. New balance: {self.player.balance}")
                    break
            print("------------------------------------\n")

            print("Dealing Cards...\n")
            self.dealer.deal(self.player)
            self.print_hands()

            ans = input("Would you like to hit? [y/n]\n")

            while ans == "y" and self.player.total < 21:
                self.dealer.deal_hit(self.player)
                if self.player.total >= 21:
                    print("BUST!!!")
                    break
                self.print_hands()
                ans = input("Would you like to hit again? [y/n]\n")

            print("\nDealer's play...\n")
            self.dealer.deal_own()
            self.print_hands()

            if self.dealer.check_win(self.player):
                print(f"YOU WIN!  +${bet}")
                self.player.balance += (2 * bet)
            else:
                print(f"Tou lose...  -${bet}")
            print(f"You new balance is: {self.player.balance}")
            print("------------------------------------\n")
            ans = input("Want to play again? [y/n]\n")
            if ans != "y":
                break
        print(f"\nFinal balance: ${self.player.balance}")

    def print_hands(self):

        print("Dealer's hand:")
        for suit, value in self.dealer.hand:
            new_value = Game.format_card(value)
            print(f"({new_value} : {suit.name.title()})", end=" ")
        print("")
        print("------------------------------------\n")

        print("Your hand:")
        for suit, value in self.player.hand:
            new_value = Game.format_card(value)
            print(f"({new_value} : {suit.name.title()})", end=" ")

        print("\n")

    @staticmethod
    def format_card(value: int) -> str:
        new_value = value
        match value:
            case 1:
                new_value = "Ace"
            case 11:
                new_value = "Jack"
            case 12:
                new_value = "Queen"
            case 13:
                new_value = "King"
        return str(new_value)


name1 = input("Enter your name.\n")
balance1 = input("Enter your balance.\n")
game = Game(name1, int(balance1))
game.play()