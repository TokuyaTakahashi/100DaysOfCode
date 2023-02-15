from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink_menu = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()


running = True
while running:
    request = input(f"What would you like? ({drink_menu.get_items()}): ")
    if request == "report":
        print(coffee_machine.report())
        print(money.report())
    elif request == "off":
        running = False
    else:
        user_drink = drink_menu.find_drink(request)
        if coffee_machine.is_resource_sufficient(user_drink):
            if money.make_payment(user_drink.cost):
                coffee_machine.make_coffee(user_drink)
        else:
            for ingredient in coffee_machine.resources:
                if coffee_machine.resources[ingredient] < user_drink.ingredients[ingredient]:
                    print(f"Sorry there is not enough {ingredient}")