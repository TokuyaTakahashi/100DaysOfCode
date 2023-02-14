import data


def resource_format(resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def count_money(coffee):
    print("Please insert coins.")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickels?: "))
    p = int(input("How many pennies?: "))
    total_cost = round((q * .25 + d * .10 + n * .05 + p * .01), 2)
    cost_of_coffee = COFFEE_MENU[coffee]["cost"]
    if total_cost > cost_of_coffee:
        change = total_cost - cost_of_coffee
        print(f"Here is ${change} in change.")
        coffee_resource['money'] += cost_of_coffee
        make_drink(coffee)
    elif total_cost == COFFEE_MENU[coffee]["cost"]:
        coffee_resource['money'] += cost_of_coffee
        make_drink(coffee)
    else:
        print("Sorry that's not enough money. Money refunded")


def make_drink(coffee):
    coffee_recipe = COFFEE_MENU[coffee]["ingredients"]
    for ing in coffee_recipe:
        coffee_resource[ing] -= recipe[ing]
    print(f"Here is your {coffee} ☕ enjoy!")


def enough_ingredients(coffee):
    for ingredient in recipe:
        if coffee_resource[ingredient] < recipe[ingredient]:
            return print(f"Sorry there is not enough {ingredient}")
    count_money(coffee)


running = True
while running:
    user = input("What would you like? (espresso/latte/cappuccino) ")
    coffee_resource = data.resources
    COFFEE_MENU = data.MENU

    if user == "report":
        resource_format(coffee_resource)
    elif user == "off":
        running = False
    elif user in ['espresso', 'latte', 'cappuccino']:
        recipe = COFFEE_MENU[user]["ingredients"]
        enough_ingredients(user)
