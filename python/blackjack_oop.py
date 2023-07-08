'''
Create a deck of 52 cards
Shuffle the deck
Ask the Player for their bet
Make sure that the Player's bet does not exceed their available chips
Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer's cards, the other remains hidden
Show both of the Player's cards
Ask the Player if they wish to Hit, and take another card
If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
Determine the winner and adjust the Player's chips accordingly
Ask the Player if they'd like to play again
'''
import random

suits =("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Queen", "Jack", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Queen":9, "Jack":8, "King":10, "Ace":11}

playing= True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
        
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has:" + deck_comp
    
    def shuffle (self):
        random.shuffle (self.deck)
        
    def deal (self):
        single_card=self.deck.pop()
        return single_card
    
class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
        
    def add_card (self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1 
        
    def adjust_for_ace(self):
        while self.value < 21 and self.aces:
            self.value -=10
            self.aces -=1 
    
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet (self):
        self.total += self.bet
        
    def lose_bet (self):
        self.total -= self.bet
        
def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input("how many chips would you play?\n"))
        except ValueError:
            print ("Sorry, must be a numeric value")
        else:
            if chips.bet > chips.total:
                print ("Man your bet can't exceed:", chips.total)
            else:
                break
            
def hit (deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand (deck, hand):
    global playing
    
    while True:
        x = input("Would you like to Hit (h) or Stand (s)?\n")
        
        if x[0].lower() == "h":
            hit (deck,hand)
        
        elif x[0].lower() == "s":
            print ("Player stands, dealer plays")
            playing = False
            
        else:
            print ("Sorry, please try again.")
            continue 
        break 
    
def show_some (player, dealer):
    
    print("\nDealer's Hand:")
    print (" <card hidden>")
    print("", dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    
def show_all (player,dealer):
    
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("Dealer's Hand=", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand=", player.value)
    
def player_bust (player, dealer, chips):
    print ("Player busts!")    
    chips.lose_bet()
    
def player_wins (player, dealer, chips):
    print ("Player wins!")
    chips.win_bet()
    
def dealer_busts(player, dealer, chips):
    print("Dealer bust!")
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print ("Dealer wins!")    
    chips.lose_bet()
    
def push(player, dealer):
    print ("tie game!")
    
while True:
    
    deck = Deck ()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand ()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    player_chips = Chips()
    
    take_bet(player_chips)    

    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck,player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_chips)
            break
    
    if player_hand.value <= 21:
    
        while dealer_hand.value < 17:
            hit (deck, dealer_hand)
        
        show_all (player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push((player_hand, dealer_hand))

    print ("Player's winnings stand at",player_chips.total)

    new_game = input ("would you like to play again?")

    if new_game[0].lower()=="y":
        playing=True
        continue
    else:
        print ("thanks for playing")
        break 
