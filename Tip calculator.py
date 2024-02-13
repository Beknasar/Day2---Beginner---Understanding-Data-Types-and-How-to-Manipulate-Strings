# Instructions
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12
#Format the result to 2 decimal places = 33.60
#Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

#Example Input
#Welcome to the tip calculator!
#What was the total bill? $124.56
#How much tip would you like to give? 10, 12, or 15? 12
#How many people to split the bill? 7

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_persent = tip / 100
total_tip_amount = bill * tip_as_persent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)
print(f"Each person should pay: {final_amount}")
