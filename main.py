# Coffee Machine - Simulates a coffee machine that contains three hot drinks as options. It prints a report on remaining
# resources to make the drinks. It accepts coins to pay for the drinks as well, and provides change.

from machine_data import MENU, resources


# Prints a report containing all resources of the machine
def print_report():
    """Returns the remaining resources within the coffee machine"""
    water_amount = resources['water']
    milk_amount = resources['milk']
    coffee_amount = resources['coffee']
    total_money = resources['money']

    print(f"Water: {water_amount}ml \nMilk: {milk_amount}ml \nCoffee: {coffee_amount}g \nMoney: ${total_money} ")


# Checks to see if there is a sufficient amount of resources to make another drink
def insufficient_resources(drink):
    """Checks to see if there is enough resources to make a hot drink (input) and returns a message to user and
    a boolean value of True if there isn't enough"""
    for item in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return True


# Process coins entered into the machine to purchase a drink
def process_coins(drink):
    """Calculates the amount of coins inserted into the machine and returns the total or change if there is any"""
    print("Please insert coins")
    price = MENU[drink]['cost']
    total_cash = 0
    change = 0
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickels = int(input("how many nickels?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01

    total_cash = quarters + dimes + nickels + pennies

    if total_cash > price:
        change = round(total_cash - price, 2)
        print(f"Here is ${change} in change.")

    return total_cash


# Checks to see if there is enough funds entered to buy a drink
def insufficient_funds(funds, drink):
    """Takes the drink and total coins entered and returns true if there is not enough funds for the transaction"""
    if funds < MENU[drink]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return True


# Makes the drink for the user and updates resources of the machine
def make_drink(drink):
    """Takes drink option from user, updates the amount of resources remaining and prints the drink the user wants"""
    if drink != "espresso":
        resources['milk'] -= MENU[drink]['ingredients']['milk']

    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']
    resources['money'] += MENU[drink]['cost']

    print(f"Here is your {drink} ☕. Enjoy!")


# Simulates a coffee machine and prompts user for an option from the menu
def coffee_machine():
    """Prompts user for a menu item, and can print a 'report' on the machine's resources or makes a drink depending on
    if there are enough resources. The machine can be turned 'off' by user"""
    machine_on = True

    while machine_on:
        menu_option = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if menu_option == "report":
            print_report()
        elif menu_option == "off":
            machine_on = False
        elif menu_option == "espresso" or menu_option == "latte" or menu_option == "cappuccino":
            if not insufficient_resources(menu_option):
                cash = process_coins(menu_option)
                if not insufficient_funds(cash, menu_option):
                    make_drink(menu_option)
        else:
            print("An incorrect menu item was entered. Please try again!")


coffee_machine()
