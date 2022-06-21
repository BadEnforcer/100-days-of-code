from machine_data import MENU, resources


def report():
    """Will print a resources report"""
    return f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee:" \
           f" {resources['coffee']}g \nMoney: ${money}"


money = 0
keep_going = True
while keep_going:
    user_choice = "report"
    while user_choice == 'report':
        user_choice = input("\nWhat would you like? (espresso/latte/cappuccino)").lower()
        if user_choice == "off":
            exit("Switching off")
        elif user_choice == "report":
            print(report())
            print("\n\n")


    def find_coffee_details(user_decision):
        return MENU[user_decision]


    def get_ingredients(coffee_flavour):
        return coffee_flavour["ingredients"]


    coffee_type = find_coffee_details(user_choice)
    basic_ingredients = get_ingredients(coffee_type)

    # ingredients
    water = int(basic_ingredients["water"])
    coffee = int(basic_ingredients["coffee"])
    if 'milk' in basic_ingredients:
        milk = int(basic_ingredients["milk"])
    cost = MENU[user_choice]['cost']

    # now minus them in the machine resources
    resources["water"] = resources["water"] - water
    resources["milk"] = resources["milk"] - milk
    resources["coffee"] = resources["coffee"] - coffee


    def check_resources(resources_dict):
        global keep_going
        if resources_dict["water"] < 0:
            print(f"Sorry ! Machine is out of resources. Refunding your money.\n")
            print(report())
            exit()
        elif resources_dict["coffee"] < 0:
            print(f"Sorry ! Machine is out of resources. Refunding your money.\n")
            print(report())
            exit()
        elif resources_dict["milk"] < 0:
            print(f"Sorry ! Machine is out of resources. Refunding your money.\n")
            print(report())
            exit()


    check_resources(resources)


    def get_money():
        quarter_amount = int(input("\nHow many quarters are you giving? ")) * 0.25
        dime_amount = int(input("How many dimes are you giving? ")) * 0.10
        nickels_amount = int(input("How many nickels are you giving? ")) * 0.05
        pennies_amount = int(input("How many pennies are you giving? ")) * 0.01
        return quarter_amount + dime_amount + nickels_amount + pennies_amount


    paid_by_user = get_money()


    def confirm_purchase(user_paid, coffee_cost, flavour):
        global money
        if user_paid == coffee_cost:
            money += coffee_cost
            return f"\nTotal cost : {coffee_cost}\nYou paid: {user_paid}.\nHere is your {flavour}. Enjoy!"
        elif user_paid > coffee_cost:
            left_money = round(user_paid - coffee_cost, 2)
            money = coffee_cost
            return f"\nTotal cost : {coffee_cost}\nYou paid: {user_paid}\n" \
                   f"Here is ${left_money} dollars in change.\nEnjoy your {flavour}."
        elif user_paid < coffee_cost:
            return f"\nNot enough money.\nTotal cost: {coffee_cost}. You paid: {round(user_paid, 2)}." \
                   f"\nRefunding Money." \
                   f"\nLet's try Again. shall we?"


    print(confirm_purchase(paid_by_user, cost, user_choice))
