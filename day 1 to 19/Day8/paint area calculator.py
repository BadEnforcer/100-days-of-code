import math


def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)  # it will round it up a number
    #  number_of_cans = round((height * width) / cover)  # will also work
    print(f"You'll need {number_of_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
