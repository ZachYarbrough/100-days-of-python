water = 300
milk = 200
coffee = 100
money = 0.0


def coffee_machine():
    global water
    global milk
    global coffee
    global money

    user_input = input("What would you like? (expresso/latte/cappuccino): ")

    if user_input == 'report':
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${round(money, 2)}")
    elif user_input == 'latte':
        if water >= 200 and milk >= 150 and coffee >= 24:
            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            current_money = ((quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01))
            if current_money == 2.5:
                water -= 200
                milk -= 150
                coffee -= 24
                money += current_money
                print('Enjoy your latte!')
            elif current_money > 2.5:
                water -= 200
                milk -= 150
                coffee -= 24
                change = current_money - 2.5
                money += current_money - change
                print(f'Enjoy your latte! Here is your change: {round(change, 2)}')
            else:
                print("Sorry you did not input enough money.")
        elif water < 200:
            print("Sorry there is not enough water.")
        elif milk < 150:
            print("Sorry there is not enough milk.")
        elif coffee < 24:
            print("Sorry there is not enough coffee.")
    elif user_input == 'expresso':
        if water >= 50 and coffee >= 18:
            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            current_money = ((quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01))
            if current_money == 1.5:
                water -= 50
                coffee -= 18
                money += current_money
                print('Enjoy your expresso!')
            elif current_money > 1.5:
                
                water -= 50
                coffee -= 18
                change = current_money - 1.5
                money += current_money - change
                print(f'Enjoy your latte! Here is your change: {round(change, 2)}')
            else:
                print("Sorry you did not input enough money.")
        elif water < 50:
            print("Sorry there is not enough water.")
        elif coffee < 18:
            print("Sorry there is not enough coffee.")
    elif user_input == 'cappuccino':
        if water >= 250 and milk >= 100 and coffee >= 24:
            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            current_money = ((quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01))
            if current_money == 3.0:
                water -= 250
                milk -= 100
                coffee -= 24
                money += current_money
                print('Enjoy your expresso!')
            elif current_money > 3.0:
                water -= 250
                milk -= 100
                coffee -= 24
                change = current_money - 1.5
                money += current_money - change
                print(f'Enjoy your latte! Here is your change: {round(change, 2)}')
            else:
                print("Sorry you did not input enough money.")
        elif water < 250:
            print("Sorry there is not enough water.")
        elif milk < 100:
            print("Sorry there is not enough milk.")
        elif coffee < 24:
            print("Sorry there is not enough coffee.")
    elif user_input == 'quit':
        print("Thanks for using the coffee machine!")
        exit()

    coffee_machine()


coffee_machine()