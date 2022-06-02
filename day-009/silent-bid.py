import os
clear = lambda: os.system('clear')

print("Welcome to the Silent Auction!")
bid_dict = []
def bidder():
    bid_name = input("What is your name: ")
    bid_price = int(input("How much do you want to bid: $"))
    bid_dict.append({
        "name": bid_name,
        "bid": bid_price
    })
    next_bid = input("Are there any other bidders? Type 'yes' or 'no'\n")
    clear()

    if next_bid == 'yes':
        bidder()
    elif next_bid == 'no':
        highest_bid = {
            "name": bid_dict[0]["name"],
            "bid": bid_dict[0]["bid"]
        }
        for bid in range(1, len(bid_dict)):
            if bid_dict[bid]["bid"] > highest_bid["bid"]:
                highest_bid = bid_dict[bid]
        print(f"Sold to {highest_bid['name']} for {highest_bid['bid']}!")

bidder()