
from random import randint
import copy

player_bank = 1000

DECK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
CARD_VALUES = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

EMPTY_HAND = {
    "cards": [],
    "isDoubled": False,
    "bet": 0,
    "isDealer": False,
}

def next_card():
    return DECK[randint(0, len(DECK) - 1)]

def deal_card_to_player(hand):
    card = next_card()
    hand["cards"].append(card)

def new_hand(isDealer, bet = 0):
    hand = copy.deepcopy(EMPTY_HAND)
    hand["isDealer"] = isDealer
    if not hand["isDealer"]:
        hand["bet"] = bet
    return hand

def get_bet(bank):
    """
    Gets a bet amount from the player.  Returns -1 if the player wants to quit.
    """
    print(f"\n\nYour current bank is: ${bank}")
    print("Minimum bet is $10, maximum bet is $100")
    print()
    bet = -1
    while bet <= 0:
        strBet = input("What is your bet for this hand? (Enter Q to quit) $ ")
        if strBet.lower() == "q":
            break
        if strBet.isdigit():
            testbet = int(strBet)
            if testbet < 10:
                print("Minimum bet is $10")
            elif testbet > bank:
                print(f"Your credit is no good here. You only have ${bank} in your bank.")
            elif testbet > 100:
                print("Maximum bet is $100")
            else:
                # Valid bet
                bet = testbet
        else:
            print(f"Invalid bet amount: {strBet}")
        if bet <= 0:
            print("Please try again.")
    return bet

def deal_hands(player_hand, dealer_hand):
    deal_card_to_player(player_hand)
    deal_card_to_player(dealer_hand)
    deal_card_to_player(player_hand)
    deal_card_to_player(dealer_hand)

def get_hand_for_display(hand, bShowHoleCard):
    strHand = ""
    for i in range(0, len(hand["cards"])):
        if i != 1 or hand["isDealer"] == False or bShowHoleCard:
            strHand += hand["cards"][i] + ' '
        else:
            strHand += "X "
    return strHand

def show_hands(player_hand, dealer_hand, bShowDealerHoleCard = False):
    bet = player_hand["bet"]
    print(f"\nBet: $ {bet}")
    print(f"\nPlayer's hand: ", get_hand_for_display(player_hand, bShowDealerHoleCard))
    print(f"\nDealer's hand: ", get_hand_for_display(dealer_hand, bShowDealerHoleCard))
    print()

def play_hand():
    bet = get_bet(player_bank);
    if bet < 0:
        return True
    player_hand = new_hand(False, bet)
    dealer_hand = new_hand(True)
    deal_hands(player_hand, dealer_hand)
    show_hands(player_hand, dealer_hand)

done = False
while not done:
    done = play_hand();
