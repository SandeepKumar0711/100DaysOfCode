print("Welcome to tip calculator!")
bill_amount = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
no_of_people = int(input("How many people to split the bill?"))
amount_to_pay = (bill_amount + ((bill_amount * tip) / 100)) / no_of_people
print("Each person should pay: $",format(amount_to_pay,".2f"))