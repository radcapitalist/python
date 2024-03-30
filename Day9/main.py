
from replit import clear
from art import logo

bids = {}
bidder = ""
while bidder != "done":
    clear()
    print(logo)
    print()
    bidder = input("Name of bidder (enter 'done' if no bidders remain): ")
    if bidder != "done":
        amount = float(input("Amount of bid: "))
        bids[bidder] = amount

high_bidder = ""
high_bid = 0
for bidder in bids:
    if bids[bidder] > high_bid:
        high_bid = bids[bidder]
        high_bidder = bidder

print(f"\nAll bids: {bids}")
print(f"\nThe high bidder is {high_bidder} with a bid of {high_bid}.\n")
