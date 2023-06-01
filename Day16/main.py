from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
billing = MoneyMachine()
machine_status = True
while machine_status:
    coffee_choice = input(f"What would you like? ({menu.get_items()}):")
    if coffee_choice == "off":
        machine_status = False
    elif coffee_choice == "report":
        coffee.report()
        billing.report()
    else:
        drink = menu.find_drink(coffee_choice)
        if drink:
            if coffee.is_resource_sufficient(drink):
                if billing.make_payment(drink.cost):
                    coffee.make_coffee(drink)
