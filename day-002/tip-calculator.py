print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

num_of_people = int(input("How many people are splitting the bill? "))

# turns the tip into a precentage
tip_as_precent = tip / 100

# Splits the bill by the number of people
split_bill = (bill / num_of_people)

# Calculates the total amount needed for each individual percent including tax
# Rounds to the second decimal
total_amount = round(split_bill * tip_as_precent + split_bill, 2)
# Formats the float to always have 2 decimal points
total_amount = "{:.2f}".format(split_bill * tip_as_precent + split_bill)

print(f"Each person should pay: ${total_amount}")