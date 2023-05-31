import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100, "cost": 0}


def make_coffee(my_coffee):
    coffee_done = True
    for key in my_coffee:
        if resources[key] > my_coffee[key]:
            resources[key] -= my_coffee[key]
        else:
            print(f"Sorry there is not enough {key}")
            return False
    return coffee_done


def billing(coffee_cost):
    coins = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    cost = (
        quarters * coins["quarters"]
        + dimes * coins["dimes"]
        + nickels * coins["nickels"]
        + pennies * coins["pennies"]
    )
    if cost >= coffee_cost:
        change = cost - coffee_cost
        return change
    return -1


os.system("cls")
run = True
while run:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input in MENU.keys():
        my_coffee = MENU[user_input]
        change = billing(my_coffee["cost"])
        if change >= 0:
            if make_coffee(my_coffee["ingredients"]):
                resources["cost"] += my_coffee["cost"]
                print(f"Here is ${change} in change.")
                print(f"Here is your {user_input}. Enjoy.")

        else:
            print("Sorry that's not enough money. Money refunded.")
    elif user_input == "off":
        run = False
    elif user_input == "report":
        for key in resources:
            if key== "cost":
                print(f"Money: {resources[key]}")
            else:
                print(f"{key}: ${resources[key]}")