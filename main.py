 
list_of_bids = []

isTrue = True
while isTrue == True:
    user_name = input("What's your name? ")
    user_bid = float(input("What's your bid amount? "))

    def dicOfNames(name ,bid):
        info = {
            "name": name,
            "bid amount": bid
        }
        list_of_bids.append(info)

    dicOfNames(name = user_name, bid = user_bid)

    addNewUser = input("Any more bids? yes or no").lower()
    if addNewUser == "yes":
        isTrue = True
    elif addNewUser == "no":
        isTrue = False
        
highestBid = {}
count = 0

for info in list_of_bids:
    if info["bid amount"] > count:
        count = info["bid amount"]
        highestBid = info

print(f"Highest bidder is, {highestBid['name']}")
