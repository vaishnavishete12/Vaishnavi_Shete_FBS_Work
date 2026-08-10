#Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#Children below 12 = 30% discount
#Senior citizen (above 59) = 50% discount
#Others need to pay full.

total = 0

for i in range(1, 6):
    print("Person", i)
    age = int(input("Enter age: "))
    ticket = float(input("Enter ticket amount: "))

    if age < 12:
        amount = ticket - (ticket * 30 / 100)
    elif age > 59:
        amount = ticket - (ticket * 50 / 100)
    else:
        amount = ticket

    total = total + amount

print("Total ticket amount for all 5 people =", total)