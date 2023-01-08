from prettytable import PrettyTable
table = PrettyTable()  # make a table
city_list = ["Las Vegas", 'New York', 'Mumbai', 'Delhi', 'Colombo', 'Rio']
city_rating = ['5 star', '5 star', "4.5 star (too many bikers)", "3 star (can't breath)", "3-4 star (never visited)",
               "3.5 star (too much jungle)"]
table.add_column("city", city_list)
table.add_column("rating", city_rating)
table.align = "c"  # change alignment
table.border = True
print(table)
