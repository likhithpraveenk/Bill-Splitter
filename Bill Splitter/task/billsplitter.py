n = int(input("Enter the number of friends joining (including you):\n"))
participants = {}
if n <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(n):
        name = input()
        participants[name] = 0
    # print(participants)
    bill = int(input("Enter the total bill value:\n"))
    rounded = round(bill / n, 2)
    for key in participants:
        participants[key] += rounded
    print(participants)
