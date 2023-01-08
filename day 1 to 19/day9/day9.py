programming_dictionary = {
    "Bug": "An error in program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    # "Loop": "The action of doing something over and over again.", 
}

print(programming_dictionary["Bug"])  # spell the key correctly

# adding new items
programming_dictionary["Loop"] = "a very good loop"
print(programming_dictionary)

# 
empty_dictionary = {}

# edit an item
programming_dictionary["Bug"] = "it's a living thing."
print(programming_dictionary["Bug"])

# loop through a dictionary
for key in programming_dictionary:
    print(key)  # giving us key
    print(programming_dictionary[key])  # giving us value of a key

# nesting list and dictionary
# example
# {
#  Key: [List], 
#  Key2:{Dict}, 
# }

capitals = {
    "France:": "Paris",
    "Germany": "Berlin",
}

# examples
travel_log = {
    "France": ["Paris", "Lille", 'Dijon'],  # it's a list
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# nesting dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", 'Dijon'], "total_visits": 12},  # it's a list
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12},
}
print(travel_log["France"])

# making it simpel
# it's a list now with dictionary's inside it
travel_log = [{
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", 'Dijon'],
        "total_visits": 12
    },  # it's a list

    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 12
     },
}]
