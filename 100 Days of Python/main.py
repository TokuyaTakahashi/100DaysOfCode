import data

# TODO: 1. Print a report of all of the coffee machine resources.


def resource_format(resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


user = input("What would you like? (espresso/latte/cappuccino)")
coffee_resource = data.resources

if user == "report":
    resource_format(coffee_resource)
