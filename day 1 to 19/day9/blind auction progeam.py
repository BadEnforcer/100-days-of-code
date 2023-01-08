from art import logo

print(logo)

stop_input = False
while not stop_input:
    # logic
    name = str(input("Please Enter you Full name : "))
    price = input("Please Enter you Bid Price $ : ")
    halt = input("Do we have more users to bid?\n(Type 'yes' or 'no')").lower()
    # logic
    bids = {name: price}
    if halt == 'yes':
        stop_input = False

    elif halt == 'no':
        stop_input = True


#

def find_highest_bidder(bidding_record):
    name_highest_bidder = ""
    highest_bid = 0
    for bidder in bidding_record:
        (bid) = int(bidding_record[bidder])
        if highest_bid < bid:
            highest_bid = bid
            name_highest_bidder = bidder
        print(f"{name_highest_bidder} is the winner with {highest_bid} $")


find_highest_bidder(bids)
# max_bid = max(bids)
# index_of_bidder = bid_price.index(max_bid)
# highest_bidder = bidders[index_of_bidder]
# print(f"The highest bidder is {highest_bidder} with {max_bid}$")


# # my method
# # from replit import clear
# from art import logo
# print(logo)

# stop_input = False
# while not stop_input:
#   #logic
#   name = str(input("Please Enter you Full name : "))
#   price = input("Please Enter you Bid Price : ")
#   halt = input("Do we have more users to bid?\solution(Type 'yes' or 'no')").lower()
#     # logic
#   bidders = []
#   bid_price = []
#   bidders.append(name)
#   bid_price.append(price)
#   if halt == 'yes':
#     stop_input = False
#     # clear()
#   elif halt == 'no':
#     stop_input = True


# max_bid = max(bid_price)
# index_of_bidder = bid_price.index(max_bid)
# highest_bidder = bidders[index_of_bidder]
# print(f"The highest bidder is {highest_bidder} with {max_bid}$")
