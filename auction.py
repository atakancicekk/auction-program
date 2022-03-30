import art

offers = {}

print(art.logo)

auction_ended = False


while auction_ended is not True:
    name = input("What's your name ?: ")
    bid = int(input("What's your bid ?: $"))

    offers[name] = bid

    more_offers = input("Are there any other bidders ? Type 'yes' or 'no'\n").lower()

    if more_offers == "no":
        highest_offered_person = ""
        highest_offer = 0
        for person in offers:
            if highest_offer <= offers[person]:
                highest_offer = offers[person]
                highest_offered_person = person
        print("The winner is " + highest_offered_person + " with a bid of $" + str(highest_offer) + ".")
        auction_ended = True

