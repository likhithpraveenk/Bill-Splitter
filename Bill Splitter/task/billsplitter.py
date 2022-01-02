import random

n = int(input("Enter the number of friends joining (including you):\n"))
participants = {}
if n <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(n):
        participants[input()] = 0
    # print(participants)
    bill = int(input("Enter the total bill value:\n"))
    rounded = round(bill / n, 2)
    for person in participants:
        participants[person] += rounded
    # print(participants)
    feature_request = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if feature_request == "Yes":
        lucky = random.choice(list(participants))
        print(f"{lucky} is the lucky one!")
        share_amount = participants[lucky]/n-1
        for person in participants:
            if person == lucky:
                participants[person] = 0
            else:
                participants[person] += share_amount
    else:
        print("No one is going to be lucky")
