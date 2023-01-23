from replit import clear

from art import logo
#HINT: You can call clear() to clear the output in the console.

def add_bidder(their_name, their_bid):
    biddings[their_name] = their_bid
    clear()

print (f"{logo}\nWelcome to the secret auction program.")
add_more = True
biddings ={}

while add_more ==True:
    bidder = input("What is your name?: ")
    bid = input("What's your bid?: ")
    add_bidder(bidder,bid)
    other_bidders= input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if other_bidders=='no':
        add_more=False

winner = ''
winning_bid = 0
for x in biddings:
    # print(f"comparing {x} 's bid of {biddings[x]} versus {winner} bid of {winning_bid}")
    if int(winning_bid) < int(biddings[x]):
        winning_bid=biddings[x]
        winner=x
print (f"The winner is {winner} with a bid of {winning_bid}")
