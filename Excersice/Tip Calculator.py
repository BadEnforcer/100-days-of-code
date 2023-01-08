print("Welcome to the tip calculator. \n")
total_bill_amount = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip = (tip_percentage / 100) * total_bill_amount
people = int(input("How many people to split bill? "))
total_per_person = round((total_bill_amount + tip) / people, 2)
result = "{:.2f}".format(total_per_person) ##using formatting to add extra zero if it isn't there
print(f"Each person should pay: ${result}")
