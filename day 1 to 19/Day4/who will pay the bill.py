import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#       METHOD 1
# num_to_select = 2
# list_of_random_items = random.sample(names, num_to_select)
# first_random_item = list_of_random_items[0]
# print(f"{first_random_item} is going to buy the meal today!")
# Method 2 tutorial
factor = random.randint(0, len(names))
p = names[factor - 1]
print(f"{p} is going to buy the meal today!")

# how it will look like with choice function
factor = random.choice(names)
print(print(f"{factor} is going to buy the meal today!"))