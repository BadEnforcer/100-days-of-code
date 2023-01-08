from prettytable import PrettyTable
print("Welcome to the theme park")
price = 0
age = int(input("How old are you? "))


def check_age(years):
    if 45 <= years < 50:
        return 0
    elif years < 12:
        return 5
    elif 12 <= years < 18:
        return 7
    elif 18 <= years <= 55:
        return 12


if check_age(age) == 0:
    print("Everything is going to be ok. have a free ride on us!")
else:
    print(f"Your Ticket Price is : {check_age(age)}")

height = int(input("How tall are you? (in centimeters) "))

should_cont = True


def check_height(h_cm):
    if h_cm < 120:
        print("Sorry! You'll have to grow taller. minimum height is 120cm")
        return False
    if h_cm > 273:
        print('You are way to tall! sorry.')
        return False
    if h_cm >= 120:
        print("Welcome aboard")
        return True


breakdown = PrettyTable()
breakdown.add_column("Category", ["Ride", "Pictures", "Total"])

while check_height(height):
    want_picture = str(input("Do you want a photo taken? ($3 charge) (Type Y or N) ")).lower()
    if want_picture == "y":
        total = price + 3
        breakdown.add_column("Cost", [f"{price}$", "3$", f"{total}$"])
        print(breakdown)
        break

    elif want_picture == "solution":
        breakdown.add_column("Cost", [f"{price}$", "0$", f"{price}$"])
        print(breakdown)
    break
