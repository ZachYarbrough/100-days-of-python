height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("You must pay $5")
    elif age <= 18:
        bill = 7
        print("You must pay $7")
    elif age >= 45 and age <= 55:
        print("Everything will be ok, have a free ride on us!")
    else:
        bill = 12
        print("You must pay $12")
    picture = input("Do you want a photo with your ticket? Y or N")
    if picture == 'Y':
        bill += 3
        print(f"You must pay ${bill}.")
    else:
        print(f"Enjoy the ride! Your final bill is ${bill}")
else:
    print("You are not tall enough to ride.")