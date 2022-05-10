from coffee_machine import MENU


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredienst are insuficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there isnot enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins insterted."""
    print("\nPlese insert coins.\n")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or Fals if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"\nHere is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("\nSorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"\nHere is your {drink_name} ☕️. Enjoy!")


profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

while is_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"\nWater: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}\n")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])