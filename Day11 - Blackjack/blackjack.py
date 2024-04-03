
from random import randint
import copy
import math
import time

player_bank = 1000

ACE = 'A'
DECK = [ACE, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
CARD_VALUES = {
    ACE: 11,
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

def evaluate_hand(hand):
    nAces = 0
    value = 0
    for card in hand["cards"]:
        value += CARD_VALUES[card]
        if card == ACE:
            nAces += 1
    while nAces > 0 and value > 21:
        value -= 10
        nAces -= 1
    return value

def get_hand_for_display(hand, bShowHoleCard):
    strHand = ""
    for i in range(0, len(hand["cards"])):
        if i != 1 or hand["isDealer"] == False or bShowHoleCard:
            strHand += hand["cards"][i] + ' '
        else:
            strHand += "X "
    if not hand["isDealer"] or bShowHoleCard:
        strHand = f"{strHand}    Value: {evaluate_hand(hand)}"
    else:
        strHand = f"{strHand}    Value: ???"
    return strHand

def show_hands(player_hand, dealer_hand, bShowDealerHoleCard = False):
    bet = player_hand["bet"]
    print(f"\nBet: $ {bet}")
    print(f"\n   Player's hand: ", get_hand_for_display(player_hand, bShowDealerHoleCard))
    print(f"\n   Dealer's hand: ", get_hand_for_display(dealer_hand, bShowDealerHoleCard))
    print()


def player_actions(player_hand, dealer_hand):
    done = False
    while not done:
        validAction = False
        validActions = ['h', 's']
        actionRequest = "What do you want to do? (H}it, (S)tay: "
        if (len(player_hand["cards"]) == 2):
            validActions = ['h', 's', 'd']
            actionRequest = "What do you want to do? (H}it, (D)ouble Down, (S)tay: "
            
        while not validAction:
            action = input(actionRequest).lower()
            if action in validActions:
                validAction = True
            else:
                print(f"Action '{action}' is not valid. Try again.")

        if action == 'h':
            deal_card_to_player(player_hand)
            newVal = evaluate_hand(player_hand)
            if newVal > 21:
                done = True
        elif action == 'd':
            player_hand["isDoubled"] = True
            deal_card_to_player(player_hand)
            done = True
        elif action == 's':
            done = True

        if not done:
            show_hands(player_hand, dealer_hand)

def dealer_actions(phand, dhand):
    while evaluate_hand(dhand) < 17:
        time.sleep(1)
        print("Dealer must take a card:")
        deal_card_to_player(dhand)
        show_hands(phand, dhand, True)

def play_hand():
    global player_bank
    def total_bet(phand, bet):
        val = bet
        if phand["isDoubled"]:
            val *= 2
        return val
    
    bet = get_bet(player_bank);
    if bet < 0:
        return True
    player_hand = new_hand(False, bet)
    dealer_hand = new_hand(True)
    deal_hands(player_hand, dealer_hand)
    show_hands(player_hand, dealer_hand)

    player_value = evaluate_hand(player_hand)
    dealer_value = evaluate_hand(dealer_hand)

    # No need to go further if the player or dealer was dealt 21 (blackjack)
    if player_value == 21 or dealer_value == 21:
        show_hands(player_hand, dealer_hand, True)
        if player_value == 21:
            if not dealer_value == 21:
                winnings = 1.5 * bet
                print(f"\nYou have Blackjack! You win $ {winnings}")
                player_bank += winnings
            else:
                print("Player and Dealer both have Blackjack. It's a push.")
        else:
            # Dealer has Blackjack, player does not
            print("Dealer has Blackjack.  You lose.")
            player_bank -= bet
    else:
        player_actions(player_hand, dealer_hand)
        show_hands(player_hand, dealer_hand, True)
        player_value = evaluate_hand(player_hand)
        full_bet = total_bet(player_hand, bet)
        if player_value > 21:
            loss = bet
            if player_hand["isDoubled"]: loss *= 2
            print(f"You busted! You lose $ {loss}")
            player_bank -= loss
        else:
            dealer_actions(player_hand, dealer_hand)
            
            dealer_value = evaluate_hand(dealer_hand)
            if dealer_value > 21:
                print(f"Dealer has busted; you win $ {full_bet}")
                player_bank += full_bet
            elif player_value > dealer_value:
                print(f"You win $ {full_bet}")
                player_bank += full_bet
            elif dealer_value > player_value:
                print(f"You lose $ {full_bet}")
                player_bank -= full_bet
            else:
                print("It's a push.")
        
done = False
while not done:
    done = play_hand();
