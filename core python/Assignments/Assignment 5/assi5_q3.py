#Accept no. of passengers from user and per ticket cost. Then accept age of each
#passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter ticket cost per passenger: "))

total_amount = 0

for i in range(passengers):
    age = int(input(f"Enter age of passenger {i + 1}: "))

    if age < 12:
        amount = ticket_cost - (ticket_cost * 0.30)   # 30% discount
    elif age > 59:
        amount = ticket_cost - (ticket_cost * 0.50)   # 50% discount
    else:
        amount = ticket_cost                          # Full ticket

    total_amount += amount

print("Total ticket amount =", total_amount)