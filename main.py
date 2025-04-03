import random

class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]
        random.shuffle(self.cards)

    def deal(self, num):
        dealt_cards = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt_cards

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def show_hand(self):
        return self.hand

class TexasHoldem:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player("Player 1"), Player("AI")]
        self.community_cards = []

    def deal_hands(self):
        for player in self.players:
            player.receive_cards(self.deck.deal(2))

    def deal_flop(self):
        self.community_cards.extend(self.deck.deal(3))

    def deal_turn(self):
        self.community_cards.extend(self.deck.deal(1))

    def deal_river(self):
        self.community_cards.extend(self.deck.deal(1))

    def show_community_cards(self):
        return self.community_cards

    def play(self):
        self.deal_hands()
        print("Hands dealt.")
        for player in self.players:
            print(f"{player.name}'s hand: {player.show_hand()}")
        
        self.deal_flop()
        print("Flop:", self.show_community_cards())
        
        self.deal_turn()
        print("Turn:", self.show_community_cards())
        
        self.deal_river()
        print("River:", self.show_community_cards())

if __name__ == "__main__":
    game = TexasHoldem()
    game.play()
