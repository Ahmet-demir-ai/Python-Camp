#deneme listeler...
"""student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Empty dictionary to store grades
student_grades = {}

Assign grades based on scores
for student in student_scores:
    score=student_scores[student]
    if score >90:
        grade = ("Outstanding")
    elif score > 80:
        grade = ("Exceeds Expectations")
    elif score > 70:
        grade = ("Acceptable")
    else:
        grade = ("Fail")
    print(student,grade)
    """

def find_highest_bidd(bidding_dictionary):
    winner=""
    highest_bid=0
    max(bidding_dictionary)

    for bid in bidding_dictionary:
        bid_amount=bidding_dictionary[bid]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bid
    print(winner,highest_bid)


bids={}
continue_bidding= True
while continue_bidding:
    name=input("name:")
    price=int(input("bid:"))
    bids[name]=price
    should_contuniue=input("are there any biddrs? yes? no?")
    if should_contuniue=="no":
        continue_bidding=  False
        find_highest_bidd(bids)
    elif should_contuniue=="yes":
        print("\n*20")
    

        


